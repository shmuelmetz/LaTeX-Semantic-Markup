# Roadmap

Tracks plans discussed for this package that live outside the code
itself — collaboration, publication, and distribution. Kept here
(committed, versioned) rather than only in chat history, after a
2026-05 plan for this exact set of topics was found to have been
made and then lost, rediscovered only by chance in 2026-09 while
digging through an old chat export.

## Collaborators

- **Josep Maria Blasco** (author of the [Rexx Parser](https://github.com/JosepMariaBlasco/rexx-parser)
  this package's sibling project, `rexx-lint`, is built on) — ongoing
  correspondence. As of 2026-09-15: replied to a second message,
  explicitly noting `rexx-lint` (a separate but related project) and
  inviting collaboration; mentioned `rxcheck` as a related tool worth
  comparing against for overlap. No collaborator has actually joined
  either project yet.

## Publication / distribution

**Goal, stated explicitly by the user 2026-09-15**: the ultimate aim
is for semantic markup — the *idea*, separating semantic intent from
typographic presentation in LaTeX — to be a first-class citizen of
the CTAN world. That is the goal, not "get this specific package onto
CTAN." If an existing CTAN package already does this well, or does it
better, contributing to or merging with that effort serves the goal
as well as or better than a solo submission of this package. Before
investing in CTAN-readiness work for this repo specifically, check
whether such a package already exists on CTAN.

- **CTAN**: a separate repo, `ctan-shmuelsemtex`, was planned back
  in 2026-05 as the actual CTAN-ready package location, distinct from
  this dev repo. It was never created — confirmed 2026-09-15
  (`gh repo view` returns not found). All real development has
  happened directly in this repo instead. **No CTAN submission has
  ever been attempted.** If/when this becomes a priority: CTAN
  expects a working documentation-PDF build (currently broken locally
  — see README's "Building" section for the known `doc.sty` issue,
  not yet root-caused), a `README`, and a CTAN catalogue entry
  (name/license/topics/version metadata) — none of that groundwork
  exists yet.
- No other distribution channel (package manager, journal
  announcement, etc.) has been discussed.

## Related papers

- [Local-Coordinate-Spaces](https://github.com/shmuelmetz/Local-Coordinate-Spaces) —
  the two papers (`LCS.arXiv.V2.tex`, `M-atlas.tex`) that use this
  package. Fully migrated onto it as of 2026-09-15 (macros, then
  bibliography, then the last decade-old "belongs in package" block).
  A further discussion — a recommendation from Claude to make M-Atlas
  a prerequisite read before LCS — is known to have happened but was
  not found on a real search of the claude.ai export (indexed at
  `Personal/personal/CHAT-INDEX-2026.md`) or this lineage's own
  86,000-line Claude Code transcript; likely lost in a ChaatGPT
  session instead. Add detail here once recovered or re-had directly.

## How to use this file

When a planning conversation about any of the above happens —
whether here, in a claude.ai chat, or elsewhere — the *decision*
belongs here, not only in that conversation's own transcript. Update
this file before ending a conversation that changes any of the above,
even if the actual code work is still pending.
