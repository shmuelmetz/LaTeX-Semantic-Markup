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

- **CTAN**: development is in this repo, and a `make ctan` target
  is to build the upload; the separate `ctan-shmuelsemtex` repo once
  planned is not needed. **No CTAN
  submission has been made.** For a submission, CTAN
  expects a working documentation-PDF build (working as of
  2026-10-10 with `xelatex`; see README's "Building" section), a
  `README`, and a CTAN catalogue entry (name/license/topics/version
  metadata) — the catalogue entry does not exist yet.
- Other channels: see step 5 below.

### Steps to submission, 2026-11-11

1. **Decide: separate package, or contribute to `mathsemantics`.**
   Ask its maintainers first, on its
   [GitHub discussions board](https://github.com/kellertuer/MathSemantics.sty/discussions).
   That repository has had no push since May 2022 and its board has
   only the welcome post, so a reply may not come; if none comes
   within a set time, go ahead separately.
2. **Fix what a reviewer would hit first.**
   - Done 2026-11-11: `\DeclareSemanticStyle` declares a style in a
     preamble. Still to do: one real journal's house style as a
     demonstration. Style switching is the package's main claim.
     Search of 2026-11-11: no journal checked imposes notation that
     differs from `default`. The AMS Style Guide (Journals, October
     2017, section 12.3.3) leaves the typeface of variables to the
     author ("Stet the author's usage") and sets the functions of its
     Appendix A in roman; Theory and Applications of Categories asks
     only for italic single characters and upright multi-character
     identifiers. The author pages found for Differential Geometry
     and its Applications, Journal of Geometry and Physics, Annals of
     Global Analysis and Geometry and manuscripta mathematica gave no
     notation rules. A demonstration style needs a journal that does
     impose conventions, or a model taken from papers it published.
   - Done 2026-11-11: moved off `l3keys2e`, which
     [CTAN marks deprecated](https://ctan.org/pkg/l3keys2e), to the
     kernel's `\ProcessKeyOptions`; dropped `xparse`. The package now
     needs LaTeX 2022-06-01 or later.
   - Review the generic command names `\set`, `\union` and
     `\intersection`; `\set` collides with `braket.sty`.
   - Choose an expl3 prefix (`l3prefixes` advises against short ones
     such as `lsm`) and register it with the LaTeX team.
   - Generalize `\Id`/`\ID`; check package options for orthogonality.
   - Bump the version and date; give the `test-*.tex` files expected
     output, so that they work as regression tests.
   - Decide whether to keep the name `shmuelsemtex`, which may read as
     a personal macro set. A rename is cheap only before submission.
3. **Package it**, per
   [CTAN's upload rules](https://ctan.org/help/upload-pkg): one
   directory named after the package, as a zip, holding the `.dtx`,
   `.ins`, documentation PDF and a UTF-8 `README.md`, without the
   generated `.sty`. The README states the license and any special
   font needs (the documentation uses David CLM for the Hebrew).
4. **Submit** through the CTAN upload form, and create the catalogue
   entry's metadata there.
5. **Get it looked at**: the LaTeX team's GitHub Discussions
   (<https://github.com/latex3/latex2e/discussions>), which replaced
   the retired LaTeX-L mailing list in 2025, for review of the
   expl3 code, ideally before submitting; TeX Stack Exchange chat,
   the other replacement, for informal discussion; TeX Stack Exchange, by
   answering real questions where the package fits; a TUGboat article
   on the journal-portability test; the sTeX and mathematical
   knowledge management community; the two papers, as real-world use.

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
