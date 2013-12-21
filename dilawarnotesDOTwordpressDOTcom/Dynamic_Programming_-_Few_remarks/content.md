~~~~ 
title: Dynamic Programming : Few remarks
type: post
status: publish
id: 291
tag: Dynamic Programming
tag: Remarks and Notes
category: Algorithms
~~~~

Why they still call it dynamic programing? I really do not know why
people are so obsessed with continuing with the established non-sense.
The name was given by Bellman, at a time when programming was an
esoteric activity practised by only few crazy people. Those days it was
not even worthy of a name.[Bellman gave it this name because it sound
impressive](http://http://www.nature.com/nbt/journal/v22/n7/full/nbt0704-909.html)
( not surprising at all since he was an American!). Both of the words
has little to do with how this method works. A more suitable name could
have been 'top-down optimization' henceforth TDO. At first look, TDO can
be mistaken seen as a recursive approach to a problem. There is a subtle
difference. Recursive method will provide a solution but they will be
painfully slower. Recursive method works very well when the
'divide-and-conquer' strategy produces a smaller problem which is
significantly smaller than the original one (say, half the size) e.g.
merge sort etc. TDO are suitable for the problem in which 'divide and
conquer' can produce subproblems which are only slightly smaller than
the original one. TDO at best can be approximated as a recursive
strategy which remembers the solutions of previously solved smaller
subproblems i.e. *memoisation* (yes, root word is memo). Almost all the
problems which can be solved by TDO can be represented by a Directed
Acyclic Graphs (DAG). Each node of this DAG represents the subproblem
and an edge between two nodes gives the 'cost' of reaching from one node
to another. The task is now reduced to find a path which maximize or
minimize this cost. Again Bellman Ford algorithm can be used to find it.
For specific problems, these methods can be improved. For example,
solving*longest increasing subsequence problem*using  TDO gives a
solution of \$latex n\^2\$ complexity. However a \$latex \\frac{n\^2}{
log(n)}\$ method was given by Masek and Paterson. END NOTES : [1]
Introduction to Algorithms, Cormen, Leiserson, Rivest and Stein [2] [See
this
document.](http://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=12LJCfglPeeb1IxC0nYWBojqT0nW7Mhu6eaQdvBlBkb8oyOiMH3J6FVOBiHtZ&hl=en_GB)
