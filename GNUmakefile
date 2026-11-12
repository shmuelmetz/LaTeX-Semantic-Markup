# GNUmakefile -- build and install the shmuelsemtex package
#
# Directory structure (all repositories side by side under one parent):
#   ../texmf/tex/latex/        STYDIR: the one directory for .sty files,
#                              shared with the papers (Local-Coordinate-Spaces)
#   LaTeX-Semantic-Markup/     this repository: shmuelsemtex.dtx and .ins
#   Local-Coordinate-Spaces/   the papers, which load the package from STYDIR
#
# Targets:
#   sty       extract shmuelsemtex.sty from shmuelsemtex.dtx (default)
#   install   copy shmuelsemtex.sty into STYDIR
#   doc       typeset shmuelsemtex.pdf (scripts/build-doc.rex)
#   check     run the regression tests in testfiles/ (l3build check)
#   ctan      check, typeset and zip the CTAN upload as
#             shmuelsemtex-ctan.zip (l3build ctan; see build.lua)
#   clean     remove TeX build leftovers
#
# Files are copied, never linked (no symlinks on JFS or FAT32).

STYDIR ?= ../texmf/tex/latex
TEX    ?= tex
REXX   ?= rexx
L3BUILD ?= l3build

.PHONY: sty install doc check ctan clean

sty: shmuelsemtex.sty

shmuelsemtex.sty: shmuelsemtex.dtx shmuelsemtex.ins
	$(TEX) shmuelsemtex.ins

install: $(STYDIR)/shmuelsemtex.sty

$(STYDIR)/shmuelsemtex.sty: shmuelsemtex.sty
	mkdir -p $(STYDIR)
	cp shmuelsemtex.sty $@

doc: shmuelsemtex.sty
	$(REXX) scripts/build-doc.rex shmuelsemtex.dtx

check:
	$(L3BUILD) check

ctan:
	$(L3BUILD) ctan

AUX_EXTS := aux log out toc idx ind ilg glo gls hd

clean:
	$(RM) $(foreach ext,$(AUX_EXTS),$(wildcard *.$(ext)))
