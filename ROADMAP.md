# Roadmap

Plans for this package outside the code itself: publication and
distribution.

## Publication / distribution

**Goal**: the ultimate aim
is for semantic markup — the *idea*, separating semantic intent from
typographic presentation in LaTeX — to be a first-class citizen of
the CTAN world. That is the goal, not "get this specific package onto
CTAN." If an existing CTAN package already does this well, or does it
better, contributing to or merging with that effort serves the goal
as well as or better than a solo submission of this package. Before
investing in CTAN-readiness work for this repo specifically, check
whether such a package already exists on CTAN.

- **CTAN**: a separate CTAN-ready repo, `ctan-shmuelsemtex`, is
  planned but not created; development is in this repo. **No CTAN
  submission has been made.** For a submission, CTAN
  expects a working documentation-PDF build (working as of
  2026-10-10 with `xelatex`; see README's "Building" section), a
  `README`, and a CTAN catalogue entry (name/license/topics/version
  metadata) — the catalogue entry does not exist yet.
- No other distribution channel (package manager, journal
  announcement, etc.) is planned yet.

### CTAN survey, 2026-10-10

Searched the CTAN catalogue (7,101 packages, via
`https://ctan.org/json/2.0/packages` and each candidate's
`/json/2.0/pkg/<name>` record) for packages that separate the meaning
of mathematical notation from its typography. Findings, from each
package's own CTAN description:

| Package | Version, date | License | Approach | Overlap with shmuelsemtex |
|---|---|---|---|---|
| `mathsemantics` (Bergmann) | 1.0.0, 2022-05-06 | MIT | Semantic commands such as `\inner{x}{y}`, grouped by topic; notation can be adapted per user | Closest in philosophy and structure. Topics (one `.sty` each): syntax, semantic, manifolds, optimization, plus abbreviations and software names. The semantic topic has some set notation (`\setDef`, `\setMid`, `\card`, `\dotcup`, `\dom`, `\image`, `\restr`). The manifolds topic is Riemannian (tangent and cotangent spaces, geodesics, exponential and logarithm maps, parallel and vector transport); it has no charts or atlases. No category-theory topic, quantifiers, or indexed unions and intersections. Repository on GitHub (kellertuer/MathSemantics.sty). |
| `semantex` (Ørsted) | 0.525, 2023-01-23 | LPPL 1.3c | Keyval-based object system for writing maths semantically; companion `stripsemantex` removes the markup for publication | Same goal, very different syntax; still beta. |
| `cool` (Setzer) | 1.35, 2023-05-03 | LGPL | Content-oriented LaTeX: keeps the meaning of expressions, aimed at conversion to Content MathML or Mathematica | Content for machine conversion, not style switching. |
| `stex` (Kohlhase, Müller) | 4.1.0, 2026-06-24 | LPPL | Semantic markup infrastructure for mathematical knowledge management | Far broader and heavier; a framework, not a notation package. |
| `nath` (Marvan) | (undated) | GPL | Context-dependent presentation from context-independent notation (fractions, delimiters) | Separates content from presentation, but at the level of layout, not named mathematical objects. |
| `substnote` (Sekorin) | 0.1.0, 2026-07-30 | MIT | One command, `\subst`, with the convention chosen once in the preamble | Same design idea (switchable convention), for a single notation. |
| `mathcommand` + `knowledge` (Colcombet) | 1.04, 2021-06-07 | LPPL 1.3 | Infrastructure for defining math macros and linking notions | Building blocks, not a notation set. |
| `semantic-markup` (Cashner) | 2020-01-29 | LPPL 1.3 | TEI-inspired semantic text markup for the humanities | Text, not maths; the reason this package was renamed. |

Scope of this package's notation: much of it is set-theoretic, or is
shared by sets and categories (dual set/category constructions),
alongside category theory, coordinate charts and atlases. Riemannian
geometry is outside its scope, though it fits the same paradigm, so
`mathsemantics`' manifolds topic does not overlap with it.

Result: no CTAN package provides semantic markup for that combination
(set-builder notation, quantifiers and indexed unions/intersections
alongside categories, morphisms, coordinate charts and atlases), and
none offers whole-package style switching aimed at different journals'
conventions. The closest existing effort is `mathsemantics`.
Contributing to it (set notation it lacks, plus a set/category topic
and charts and atlases) is the option that best fits the stated goal
and should be weighed against a separate submission of this package.
`substnote` shows that CTAN accepts small packages built on the same
switchable-convention idea. Not yet decided.

## Related papers

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) —
  the two papers (`LCS.arXiv.V2.tex`, `M-atlas.tex`) that use this
  package. Fully migrated onto it as of 2026-09-15 (macros, then
  bibliography, then the last decade-old "belongs in package" block).
- Open question: whether M-Atlas should be read before LCS.
