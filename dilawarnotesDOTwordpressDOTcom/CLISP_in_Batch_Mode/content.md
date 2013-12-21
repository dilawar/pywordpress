~~~~ 
title: CLISP in Batch Mode
type: post
status: publish
id: 420
tag: clisp batch
tag: clisp non-interactive ode
category: LISP
category: Programming
~~~~

I struggled few hours to get CLisP working in batch mode (Of course,
Internet was down in my room). Here is what I followed to get it working
in script mode. Look at this [article](http://cybertiggyr.com/lscript/).
Also there is cross-platform LISP interface [\$latex
\\lambda\$-gtk](http://common-lisp.net/project/lambda-gtk/) . The
simplest way to do it was to write the function etc in a text file and
use 'load' command in CLISP interpreter. [sourcecode] (load "filename")
[/sourcecode] That all folks!
