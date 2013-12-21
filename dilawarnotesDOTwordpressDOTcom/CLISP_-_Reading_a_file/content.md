~~~~ 
title: CLISP : Reading a file
type: post
status: publish
id: 423
tag: lisp
tag: lisp read file
category: LISP
category: Programming
~~~~

See the references at the end of this post for details related with this
topic. It will help you learn all the nuts and bolts of streams handling
in clisp. Now I want to read this file which contain following
information. To be precise, its a graph written in a format which
resembles lisp code. [sourcecode language="text"] (a) (b c d) (b) (a c
d) (c) (a b d) (d) (b c) [/sourcecode] It graph file can be very
complicated. Here is what I did to read this file. What each line does
in code can be googled out easily. Just put lisp with the keyword while
searching. [sourcecode language="text"] ; Dilawar Singh ; 2011, IIT
Bombay ; Dept of Electrical Engineering. ;; This function will open a
file and read a graph. ;; TODO : Graph Format. ;; ;;; THIS SECTION OPEN
A FILE AND READ IT. ;;;; TODO: File name should be passed from terminal.
For now we assume that file ;;;; name is 'graph.txt' by dafault and it
reside is the same directory as of this ;;;; file containing source
code. (with-open-file (graph-stream "./graph.txt" :direction :input
:if-does-not-exist :create) (loop for line = (read-line graph-stream nil
'end-of-graph) until(eq line 'end-of-graph) do( print line))) ;; We need
to something more. [/sourcecode] References :
[1] [http://www.lispworks.com/documentation/HyperSpec/Body/v\_debug\_.htm](http://www.lispworks.com/documentation/HyperSpec/Body/v_debug_.htm)
[2] [http://cl-cookbook.sourceforge.net/os.html](http://cl-cookbook.sourceforge.net/os.html)
[3] [http://cl-cookbook.sourceforge.net/files.html](http://cl-cookbook.sourceforge.net/files.html#line)
[4] [http://www.gnu.org/software/emacs/elisp/html\_node/Input-Streams.html\#Input-Streams](http://www.gnu.org/software/emacs/elisp/html_node/Input-Streams.html#Input-Streams)
