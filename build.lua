-- build.lua -- l3build configuration for semanticmath
--
--   l3build check   run the regression tests in testfiles/
--   l3build save X  record testfiles/X.tlg after checking its output by hand
--   l3build doc     typeset semanticmath.pdf
--   l3build ctan    check, typeset and zip the CTAN upload
--
-- The documentation needs XeLaTeX (fontspec, for the Hebrew in the
-- author line); the tests run under pdfLaTeX.

module        = "semanticmath"

sourcefiles   = { "semanticmath.dtx", "semanticmath.ins" }
unpackfiles   = { "semanticmath.ins" }
installfiles  = { "semanticmath.sty" }
typesetfiles  = { "semanticmath.dtx" }
textfiles     = { "README.md", "LICENSE" }
ctanreadme    = "README.md"

typesetexe    = "xelatex"
checkengines  = { "pdftex" }
stdengine     = "pdftex"
checkruns     = 1
testfiledir   = "testfiles"
