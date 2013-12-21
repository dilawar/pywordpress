~~~~ 
title: Python front-end for Noweb literate tool 
type: post
status: publish
id: 999
tag: literate programming
tag: literate programming tool
category: Programming
~~~~

The idea behind literate programming, that a program can be a piece of
literature, is due to [Donald E.
Knuth](http://www-cs-faculty.stanford.edu/%7Euno/). Knuth is an
extremely respected figure in programming community (and also among
combinatorics and computer science people). In this paradigm, one does
not write a program based on how computer would reason about it but
rather follows a human like flow. It is the job of literate programming
tool to convert this human-readable program into something which make
sense to a computer. There is much freedom for a programmer to write his
code the way he likes it but since the translation process is governed
by a computer program, there are specific constraints on how to write a
program in literate way. Best way to understand the difference between a
normally commented and literate program is to have a look at a literate
program. One can easily find many on Knuth’s home page. A program is
written like an essay, and one then uses a tool to extract code (this
process was called `tangling` by Knuth) or documentation (process called
`weaving`) out of it. Knuth, true to his nature, wrote `cweb` for his
personal use. Some other tools cropped up on these lines and many of
them were written for pacific languages. Noweb, written by Roman Ramsay,
is language agnostic. There are some other tools like it e.g.
funnel-web, nuweb etc but none is as simple to use as this one.
[Lyx](http://www.lyx.org "LyX") also have support for
[noweb](http://www.cs.tufts.edu/~nr/noweb/ "Noweb"). And if my memory
serves me write, IIT Madras, offered (or still offering) a course in
literate programming to its students using Lyx. Literate programming did
not really catch up (who wants to write documentation in the first
place). But some people have used it extensively. To my knowledge, apart
from Knuth, Columbia Esterel Compiler (cec) is written as literate
program using noweb and its really easy to understand (well, not really
but relatively). I was able to make changes to it for my personal
**fun**.

### A python front-end for noweb

[Script is
here](https://github.com/dilawar/Scripts/blob/master/pynoweb.py) I found
one thing lacking in noweb that I have to write full program in one file
or use makefiles to automate the process. This is OK but I was not
happy. I wrote a python script to do the following,

-   There is one main file which include other files using
    `%\include{file.nw}` macro. Notice that this approach is like tex.
    Our macro will be treated as comment by normal tex program but not
    by this python front-end.
-   Write as many noweb files as you like and using `%\include` macro to
    include other literate files.
-   Pass the main file to python script with optional command (tangling
    or weaving)
-   You can attach a line over chunk name to tell this script that you
    want to write this chunk to some specific file. Write over the chunk
    something like `%file:src/file.c`. For example, if a chunk named
    `gloabal.h` is to be written to file `include/global.h` then, just
    above the chunk `<<global.h>>`, you must have

<!-- -->

       %file:include/global.h
       <>=
       // whatver is there in global
       @ %def global.h 

Download the script and run it without any argument to see the possible
commands. Report an issue on its github repo if you locate a bug.

 
