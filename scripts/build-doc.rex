#!/usr/bin/env rexx
/* build-doc.rex -- typeset a .dtx package documentation file
 *
 * Usage: rexx build-doc.rex [file.dtx]      (default: shmuelsemtex.dtx)
 *
 * Runs in the directory that holds the .dtx file.  Extracts the .sty
 * with TeX from the matching .ins file, then runs XeLaTeX as many
 * times as the cross-references need (as the papers are built), with
 * makeindex for the index and the change history after the first pass.
 * Requires ooRexx 5 (ADDRESS ... WITH).
 */
parse arg dtx .
if dtx = '' then dtx = 'shmuelsemtex.dtx'
full = stream(dtx, 'C', 'QUERY EXISTS')
if full = '' then do
  say 'build-doc: cannot find' dtx
  exit 1
end
call directory filespec('Location', full)
name = filespec('Name', full)
job = name~left(name~lastPos('.') - 1)

if run('tex -interaction=nonstopmode' job'.ins') then exit 1

maxPasses = 5
do pass = 1 to maxPasses
  if stream(job'.pdf', 'C', 'QUERY EXISTS') \= '',
     & stream(job'.pdf', 'C', 'OPEN WRITE') \= 'READY:' then do
    say 'build-doc:' job'.pdf is in use (open in a viewer?); close it and rerun'
    exit 1
  end
  call stream job'.pdf', 'C', 'CLOSE'
  if run('xelatex -interaction=nonstopmode -halt-on-error' job'.dtx') then do
    say 'build-doc: XeLaTeX failed on pass' pass'; see' job'.log'
    exit 1
  end
  if pass = 1 then do
    if stream(job'.idx', 'C', 'QUERY EXISTS') \= '' then
      call run 'makeindex -q -s gind.ist -o' job'.ind' job'.idx'
    if stream(job'.glo', 'C', 'QUERY EXISTS') \= '' then
      call run 'makeindex -q -s gglo.ist -o' job'.gls' job'.glo'
  end
  else if \needsRerun(job'.log') then leave
end

if pass > maxPasses then say 'build-doc: references still unsettled after' maxPasses 'passes'
else say 'build-doc:' job'.pdf built in' pass 'passes'
exit 0

/* Run a command quietly; on failure show its last lines, return .true */
::routine run
  use strict arg command
  out = .array~new
  err = .array~new
  address system command with output using (out) error using (err)
  if rc = 0 then return .false
  say 'build-doc: "'command'" ended with return code' rc
  do line over out~section(max(1, out~items - 5))
    say '  ' line
  end
  do line over err
    say '  ' line
  end
  return .true

/* Does the log ask for another pass? */
::routine needsRerun
  use strict arg logName
  log = .stream~new(logName)
  text = log~arrayIn~makeString('LINE', ' ')
  log~close
  return text~pos('Rerun to get') > 0,
       | text~pos('Label(s) may have changed') > 0,
       | text~pos('There were undefined references') > 0
