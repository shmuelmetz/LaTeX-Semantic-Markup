-- build.lua -- l3build configuration for shmuelsemtex
--
--   l3build check   run the regression tests in testfiles/
--   l3build save X  record testfiles/X.tlg after checking its output by hand
--   l3build doc     typeset shmuelsemtex.pdf
--   l3build ctan    check, typeset and zip the CTAN upload
--
-- The documentation needs XeLaTeX (fontspec, for the Hebrew in the
-- author line); the tests run under pdfLaTeX.

module        = "shmuelsemtex"

sourcefiles   = { "shmuelsemtex.dtx", "shmuelsemtex.ins" }
unpackfiles   = { "shmuelsemtex.ins" }
installfiles  = { "shmuelsemtex.sty" }
typesetfiles  = { "shmuelsemtex.dtx" }
textfiles     = { "README.md", "LICENSE" }
ctanreadme    = "README.md"

typesetexe    = "xelatex"
checkengines  = { "pdftex" }
stdengine     = "pdftex"
checkruns     = 1
testfiledir   = "testfiles"
