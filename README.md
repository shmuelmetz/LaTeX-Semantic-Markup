# LaTeX-Semantic-Markup

Semantic markup macros for LaTeX, written in expl3 (LaTeX3).

Author: Shmuel (Seymour J.) Metz
(<https://mason.gmu.edu/~smetz3>)

## Purpose

This package provides macros that separate semantic intent from
typographic presentation in LaTeX documents, in the spirit of the
expl3 programming layer. Rather than writing `\mathscr{A}` directly
whenever a symbol names a category, an author writes `\catName{A}`
and the presentation is defined separately.

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
cp *.sty $(kpsewhich -var-value TEXMFHOME)/tex/latex/semantic-markup/
mktexlsr
```

## Usage

```latex
\usepackage{semantic-markup}
```

```latex
$\catName{A}$        % display name of a category
$\catSeqName{A}$      % display name of a sequence/family of categories
$\objName{x}$        % display name of an object
$\morphName{f}$      % display name of a morphism
$\morphSeqName{f}$   % display name of a sequence/tuple of morphisms
$\morphMono$ $\morphEpi$  % monomorphism / epimorphism arrows
$\morphCompose$ / $\morphComposeHead$ / $\morphComposeTail$  % composition (plain / head / tail; each also takes [label])
$\chartName{U}$ $\atlasName{A}$ $\coordName{x}$  % coordinate charts/atlases/coordinates
```

The full macro set, including which abbreviations each name uses and
several open mathematical questions not yet settled, is documented
in `semantic-markup.dtx` (build the typeset manual, once the local
toolchain issue below is resolved, with `pdflatex semantic-markup.dtx`).

## Design goal: house-style portability

The package's actual purpose, in the author's words: *if you submit
a paper to different journals, you shouldn't have to change your
markup to accommodate different house styles, other than changing
setup.* Concretely: `\catName{Set}` (or any semantic macro, anywhere
in the document body) is byte-for-byte identical regardless of the
target -- arXiv, journal X's house style, journal Y's house style.
Only *setup* changes, in either of two equivalent forms:

```latex
\usepackage[style=default]{semantic-markup}   % at load time, built in
\usepackage[style=plain]{semantic-markup}     % at load time, built in
```
```latex
\setupsemanticmarkup{style=plain}             % anywhere in the body
```

`style` defaults to `default` (no options needed at all). Every
built-in style reassigns the package's complete set of internal
presentation hooks as one coherent bundle -- never a partial patch
the author assembles by hand -- so adding a real journal's house
style later means adding one more style, not touching any document
body. See `semantic-markup.dtx`, "Style switching", for the full
mechanism (`l3keys2e`) and design rationale.

The runtime form, `\setupsemanticmarkup`, matches an established,
already-proven pattern already used in the source papers themselves
(`LCS.arXiv.V2.tex`/`M-atlas.tex`'s own `\setupquant`/`\setupset`
commands, built on plain `l3keys`, called once in the document body
separately from every use site) -- not invented from scratch, and
kept alongside the package-option form since both are legitimate
(the runtime form additionally works mid-document, where a package
option cannot).

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
tex semantic-markup.ins      # extracts semantic-markup.sty from the .dtx
pdflatex semantic-markup.dtx # typesets the documentation PDF
```

The generated `semantic-markup.sty` is not committed to this
repository (see `.gitignore`) -- it is reproducible from
`semantic-markup.dtx` via the `.ins` file above, per standard
practice for `.dtx`-based packages.

As of this writing, the documentation-PDF build
(`pdflatex semantic-markup.dtx`) fails on at least one local MiKTeX
installation with `! File ended while scanning use of \xmacro@code.`,
reproducible even with a trivial `\begin{macrocode}\relax\end{macrocode}`
under plain `ltxdoc` -- i.e. it is a local `doc.sty` (v3.0r,
2026-03-13) issue, not a problem in this package's `.dtx` content.
`tex semantic-markup.ins` (the actual `.sty` extraction) is unaffected
and has been verified to compile and run correctly in a real document.

## Repository structure

```
semantic-markup.dtx    -- documented source (macros + documentation)
semantic-markup.ins    -- docstrip installer; extracts the .sty
test-doc.tex            -- manual smoke test exercising every macro
test-body.tex           -- shared document body for the style tests below
test-style-default.tex  -- \usepackage[style=default]{semantic-markup} + test-body.tex
test-style-plain.tex    -- \usepackage[style=plain]{semantic-markup} + test-body.tex
test-style-noopts.tex   -- \usepackage{semantic-markup} (no options) + test-body.tex
test-setup-runtime.tex  -- \setupsemanticmarkup{...} called mid-document
test-catname-decoration.tex -- regression test for \catName's auto-detection
                             against every real argument found in the source
                             papers (17 unique arguments, 3413 call sites)
```

## Related

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) --
  mathematical papers that use these macros
- arXiv author page: <http://arxiv.org/a/metz_s_1>

## License

MIT License. See [LICENSE](LICENSE).
