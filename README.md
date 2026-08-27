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
$\morphMono$ $\morphEpi$  % monomorphism / epimorphism arrows
$\morphCompose$ or $\morphCompose[label]$  % composition, plain or labeled
$\chartName{U}$ $\atlasName{A}$ $\coordName{x}$  % coordinate charts/atlases/coordinates
```

The full macro set, including which abbreviations each name uses and
several open mathematical questions not yet settled, is documented
in `semantic-markup.dtx` (build the typeset manual, once the local
toolchain issue below is resolved, with `pdflatex semantic-markup.dtx`).

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
semantic-markup.dtx   -- documented source (macros + documentation)
semantic-markup.ins   -- docstrip installer; extracts the .sty
test-doc.tex           -- manual smoke test exercising every macro
```

## Related

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) --
  mathematical papers that use these macros
- arXiv author page: <http://arxiv.org/a/metz_s_1>

## License

MIT License. See [LICENSE](LICENSE).
