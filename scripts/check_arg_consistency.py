#!/usr/bin/env python3
"""check_arg_consistency.py -- verify \\lsm_if_arbitrary_symbol:nTF (the
auto-detection behind \\catName/\\morphName/\\morphSeqName) against every
real argument a given macro is actually called with in one or more real
.tex files, before trusting a rename or a heuristic change.

This is exactly the tool used to find and fix two real bugs in this
package: \\catName misclassifying \\catname{C^2}/\\catname{E^i}/
\\catname{XY} under an earlier single-token-only test, and the same
class of bug in \\morphName/\\morphSeqName once the papers' real
\\funcname/\\funcseqname definition was found. See semantic-markup.dtx's
"Tightened, 2026-09-01" corrections for the writeups those runs
produced.

What it does, in order:
  1. Scans each input .tex file for every `\\<macro>{...}` call
     (balanced-brace aware), for each macro name given.
  2. Deduplicates by argument text, recording which macro(s) called
     each one (real papers tend to have a small vocabulary of
     arguments repeated at thousands of call sites -- deduplicating
     first keeps the actual pdflatex run fast).
  3. Writes a pdflatex-ready .tex harness that calls
     \\lsm_if_arbitrary_symbol:nTF on every unique argument and prints
     which branch fired.
  4. Runs pdflatex on that harness (needs `semantic-markup.sty` on
     TEXINPUTS -- run `tex semantic-markup.ins` in this repo first)
     and reports one RESULT line per unique argument.

Usage:
    python scripts/check_arg_consistency.py --macro catname --macro cat \\
        path/to/paper1.tex path/to/paper2.tex

    # then cross-check each RESULT's "single=YES/NO" against which
    # macro that argument was actually called with in the source, the
    # same way the semantic-markup.dtx corrections did by hand.

Requires a `pdflatex` on PATH and `semantic-markup.sty` reachable via
TEXINPUTS (or copied next to the generated harness).
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

BACKSLASH = chr(92)


def extract_calls(text, macro):
    """Every `\\macro{...}` call in text, balanced-brace aware.
    Returns a list of (position, argument) tuples."""
    pat = re.compile(re.escape(BACKSLASH + macro) + r'\{')
    results = []
    for m in pat.finditer(text):
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth > 0:
            c = text[i]
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            i += 1
        if depth == 0:
            results.append((m.start(), text[start:i - 1]))
    return results


def collect_unique_args(paths, macros):
    """arg text -> set of macro names it was called with, across all files."""
    unique = {}
    for path in paths:
        with open(path, encoding='utf-8', errors='replace') as f:
            text = f.read()
        for macro in macros:
            for _, arg in extract_calls(text, macro):
                unique.setdefault(arg, set()).add(macro)
    return unique


def write_harness(unique, out_path):
    items = sorted(unique.items(), key=lambda kv: kv[0])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(
            "\\documentclass{article}\n"
            "\\usepackage{semantic-markup}\n"
            "\\ExplSyntaxOn\n"
            "\\cs_new_protected:Npn \\lsmCheckOne #1#2#3\n"
            "  {\n"
            "    \\lsm_if_arbitrary_symbol:nTF {#3}\n"
            "      { \\iow_term:x { RESULT~#1~~macro=#2~~"
            "arg=\\tl_to_str:n{#3}~~single=ARBITRARY } }\n"
            "      { \\iow_term:x { RESULT~#1~~macro=#2~~"
            "arg=\\tl_to_str:n{#3}~~single=NAMED } }\n"
            "  }\n"
            "\\ExplSyntaxOff\n"
            "\\begin{document}\n"
        )
        for i, (arg, macros) in enumerate(items):
            macro_tag = ','.join(sorted(macros))
            f.write(f"\\lsmCheckOne{{{i}}}{{{macro_tag}}}{{{arg}}}\n")
        f.write("Done.\n\\end{document}\n")
    return items


def run_pdflatex(tex_path):
    workdir = os.path.dirname(tex_path) or '.'
    result = subprocess.run(
        ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
         os.path.basename(tex_path)],
        cwd=workdir, capture_output=True, text=True,
    )
    return result.stdout + result.stderr


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                      formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--macro', action='append', required=True,
                         help='macro name (no backslash), repeatable')
    parser.add_argument('files', nargs='+', help='.tex file(s) to scan')
    parser.add_argument('--keep', action='store_true',
                         help='keep the generated harness .tex/.log instead of '
                              'deleting it from the temp directory')
    args = parser.parse_args()

    unique = collect_unique_args(args.files, args.macro)
    print(f'{len(unique)} unique argument(s) across {len(args.files)} file(s) '
          f'and {len(args.macro)} macro(s)', file=sys.stderr)

    tmpdir = tempfile.mkdtemp(prefix='lsm-check-')
    tex_path = os.path.join(tmpdir, 'check-arg-consistency.tex')
    items = write_harness(unique, tex_path)

    log = run_pdflatex(tex_path)
    for line in log.splitlines():
        if line.startswith('RESULT'):
            print(line)

    if 'Fatal error' in log:
        print('pdflatex reported a fatal error -- see full log below:',
              file=sys.stderr)
        print(log, file=sys.stderr)
        sys.exit(1)

    if args.keep:
        print(f'harness kept at {tex_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
