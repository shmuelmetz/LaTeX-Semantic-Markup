# LaTeX-Semantic-Markup

Semantic markup macros for LaTeX, written in expl3 (LaTeX3).

Author: Seymour J. Metz (H: Shmuel שמואל בן לייביש ולאה)
(<https://mason.gmu.edu/~smetz3>)

## Purpose

This package provides macros that separate semantic intent from
typographic presentation in LaTeX documents, in the spirit of the
expl3 programming layer. Rather than writing `\mathscr{A}` directly
whenever a symbol names a category, an author writes `\catName{A}`
and the presentation is defined separately. This category-theory
naming layer (`\catName`, `\morphName`, `\morphMono`/`\morphEpi`,
etc.) is only part of the package: quantifiers (`\equant`/`\uquant`)
and set-builder notation (`\set`/`\union`/`\intersection`) are
general first-order-logic and set-theory constructs, not specific to
category theory, and are equally usable in any mathematical document.

## Requirements

- A current TeX Live or MiKTeX distribution
- The `expl3` package (part of the LaTeX3 bundle, included in all
  modern distributions)
- LaTeX2e with the `xparse` package (also included in modern
  distributions)

## Installation

### For a single project

Copy the `.sty` file(s) into your project directory.

### System-wide (TeX Live)

```sh
cp *.sty $(kpsewhich -var-value TEXMFHOME)/tex/latex/shmuelsemtex/
mktexlsr
```

## Usage

```latex
\usepackage{shmuelsemtex}
```

```latex
$\catName{A}$        % display name of a category
$\catSeqName{A}$      % display name of a sequence/family of categories
$\objName{x}$        % display name of an object
$\morphName{f}$      % display name of a morphism
$\morphSeqName{f}$   % display name of a sequence/tuple of morphisms
$\morphMono$ $\morphEpi$  % monomorphism / epimorphism arrows
$\morphCompose$ / $\morphComposeHead$ / $\morphComposeTail$  % composition (plain / head / tail; each also takes [label])
$\chartName{U}$ $\atlasName{A}$ $\coordName{x}$  % charts/atlases/coordinates
```

The full macro set, including which abbreviations each name uses and
several open mathematical questions not yet settled, is documented
in `shmuelsemtex.dtx` (see "Building" below for the typeset
manual).

## Design goal: house-style portability

A paper submitted to different journals should not need different
markup for their different house styles, only different setup.
Concretely: `\catName{Set}` (or any semantic macro, anywhere
in the document body) is byte-for-byte identical regardless of the
target -- arXiv, journal X's house style, journal Y's house style.
Only *setup* changes. The overall style is set as a package option
or with `\setupsemanticmarkup`:

```latex
\usepackage[style=default]{shmuelsemtex}   % at load time, built in
\usepackage[style=plain]{shmuelsemtex}     % at load time, built in
```
```latex
\setupsemanticmarkup{style=plain}             % anywhere in the body
```

Quantifier and set-builder rendering have their own setup commands,
`\setupquant` and `\setupset`.

`style` defaults to `default` (no options needed at all). Every
built-in style reassigns the package's complete set of internal
presentation hooks as one coherent bundle -- never a partial patch
the author assembles by hand -- so adding a real journal's house
style later means adding one more style, not touching any document
body. See `shmuelsemtex.dtx`, "Style switching", for the full
mechanism (`l3keys2e`) and design rationale.

`\setupsemanticmarkup` follows the same pattern as `\setupquant` and
`\setupset`: a runtime command built on plain `l3keys`, called away
from the use sites, which also works mid-document, where a package
option cannot.

`test-body.tex` plus `test-style-default.tex` / `test-style-plain.tex`
/ `test-style-noopts.tex` demonstrate and verify the package-option
form: the same `\input{test-body.tex}` body, unmodified, renders
differently under each `\usepackage[style=...]` line, and the
no-options case matches `style=default` exactly. `test-setup-runtime.tex`
demonstrates and verifies the runtime form: the same macro use sites
render under `default`, then `plain`, then back to `default`, purely
by way of three `\setupsemanticmarkup{...}` calls placed away from
the use sites, mirroring the papers' own `\setupquant` usage.

## Building

```sh
rexx scripts/build-doc.rex shmuelsemtex.dtx
```

`scripts/build-doc.rex` (ooRexx 5) works in the directory holding the
`.dtx`. It extracts `shmuelsemtex.sty` with `tex shmuelsemtex.ins`,
runs `xelatex shmuelsemtex.dtx`, builds the index and change history
with `makeindex`, and reruns XeLaTeX until the cross-references and
page references settle (normally three passes in all). By hand:

```sh
tex shmuelsemtex.ins
xelatex shmuelsemtex.dtx
makeindex -s gind.ist -o shmuelsemtex.ind shmuelsemtex.idx
makeindex -s gglo.ist -o shmuelsemtex.gls shmuelsemtex.glo
xelatex shmuelsemtex.dtx
xelatex shmuelsemtex.dtx
```

The documentation loads `fontspec` for the Hebrew in the author
line, so it needs XeLaTeX (or LuaLaTeX); `pdflatex` stops with a
fontspec error. It also loads `cleveref`, and writes cross-references
as "section N (Title) on page P", as the papers do.

The generated `shmuelsemtex.sty` is not committed to this
repository (see `.gitignore`) -- it is reproducible from
`shmuelsemtex.dtx` via the `.ins` file above, per standard
practice for `.dtx`-based packages.

In the `.dtx`, every `\begin{macrocode}` and `\end{macrocode}` line
must be `%` followed by exactly four spaces: `doc` recognizes the end
of a code block only in that form, and with any other spacing it
reads on to the end of the file (`! File ended while scanning use of
\xmacro@code.`).

## Repository structure

```
shmuelsemtex.dtx    -- documented source (macros + documentation)
shmuelsemtex.ins    -- docstrip installer; extracts the .sty
test-doc.tex            -- manual smoke test exercising every macro
test-body.tex           -- shared document body for the style tests below
test-style-default.tex  -- \usepackage[style=default]{shmuelsemtex} + test-body.tex
test-style-plain.tex    -- \usepackage[style=plain]{shmuelsemtex} + test-body.tex
test-style-noopts.tex   -- \usepackage{shmuelsemtex} (no options) + test-body.tex
test-setup-runtime.tex  -- \setupsemanticmarkup{...} called mid-document
test-catname-decoration.tex -- regression test for \catName's auto-detection
                             against every real argument found in the source
                             papers (17 unique arguments, 3413 call sites)
test-morphname-decoration.tex -- same regression test for \morphName/
                             \morphSeqName (11 unique arguments, 5409 calls)
scripts/check_arg_consistency.py -- reusable tool: given a macro name and
                             one or more real .tex files, checks every
                             unique real argument against
                             \lsm_if_arbitrary_symbol:nTF, for checking a
                             rename or a change to the classification test
scripts/build-doc.rex    -- builds the documentation PDF (see Building)
```

## Related

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) --
  mathematical papers that use these macros
- arXiv author page: <http://arxiv.org/a/metz_s_1>
- Stack Exchange: <https://stackexchange.com/users/8873368/shmuel>;
  TeX Stack Exchange: <https://tex.stackexchange.com/users/110591/shmuel>

## License

MIT License. See [LICENSE](LICENSE).
