# LaTeX-Semantic-Markup

Semantic markup macros for LaTeX, written in expl3 (LaTeX3).

Author: Shmuel (Seymour J.) Metz
(<https://mason.gmu.edu/~smetz3>)

## Purpose

This package provides macros that separate semantic intent from
typographic presentation in LaTeX documents, in the spirit of the
expl3 programming layer. Rather than writing `\textit{genus name}`
directly, an author writes `\taxon{genus name}` and the presentation
is defined separately.

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

See the documentation (TODO: add .dtx/.pdf) for available macros.

## Repository structure

```
TODO: populate as files are added
```

## Related

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) --
  mathematical papers that use these macros
- arXiv author page: <http://arxiv.org/a/metz_s_1>

## License

MIT License. See [LICENSE](LICENSE).
