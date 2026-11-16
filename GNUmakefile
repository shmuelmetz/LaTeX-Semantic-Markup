# GNUmakefile -- build and install the semanticmath package
#
# Directory structure (all repositories side by side under one parent):
#   ../texmf/tex/latex/        STYDIR: the one directory for .sty files,
#                              shared with the papers (Local-Coordinate-Spaces)
#   LaTeX-Semantic-Markup/     this repository: semanticmath.dtx and .ins
#   Local-Coordinate-Spaces/   the papers, which load the package from STYDIR
#
# Targets:
#   sty       extract semanticmath.sty from semanticmath.dtx (default)
#   install   copy semanticmath.sty into STYDIR
#   doc       typeset semanticmath.pdf (scripts/build-doc.rex)
#   check     run the regression tests in testfiles/ (l3build check)
#   ctan      check, typeset and zip the CTAN upload as
#             semanticmath-ctan.zip (l3build ctan; see build.lua)
#   clean     remove TeX build leftovers
#
# Files are copied, never linked (no symlinks on JFS or FAT32).

STYDIR ?= ../texmf/tex/latex
TEX    ?= tex
REXX   ?= rexx
L3BUILD ?= l3build

.PHONY: sty install doc check ctan clean

sty: semanticmath.sty

semanticmath.sty: semanticmath.dtx semanticmath.ins
	$(TEX) semanticmath.ins

install: $(STYDIR)/semanticmath.sty

$(STYDIR)/semanticmath.sty: semanticmath.sty
	mkdir -p $(STYDIR)
	cp semanticmath.sty $@

doc: semanticmath.sty
	$(REXX) scripts/build-doc.rex semanticmath.dtx

check:
	$(L3BUILD) check

ctan:
	$(L3BUILD) ctan

AUX_EXTS := aux log out toc idx ind ilg glo gls hd

clean:
	$(RM) $(foreach ext,$(AUX_EXTS),$(wildcard *.$(ext)))
