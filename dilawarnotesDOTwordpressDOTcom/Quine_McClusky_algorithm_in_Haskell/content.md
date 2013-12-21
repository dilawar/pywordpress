~~~~ 
title: Quine McClusky algorithm in Haskell
type: post
status: publish
id: 593
tag: Quine McClusky
tag: Quine-McClusky algorithm in haskell
category: Algorithms
category: Boolean-algebra
category: Haskell
~~~~

A small program tingu is implemented in haskell. It reads minterms from
a file and produce the output on console. It is hosted on
[github](https://github.com/dilawar/ee677/tree/master/Assignment01/haskell).
You can use it like

     ./tingu -i minterms 

Your minterms should be described in a file like following

     vars = 4
    minterms = 1,2,5,7,8,9,10,13,15, 

Then output of program is

     Hello, I am Tingu, the mighty crab! And I like tea. You should call me $./tingu -i filename from your terminal. 
    ** I have found the essential prime implicants of your function. 
      0-01 
      -001 
      010- 
      10-- 
      1-1- 
    ** Verifying my answers. It may take some time.... 
    +++ OK, passed 100 tests. Peace!! 

Peace !!
