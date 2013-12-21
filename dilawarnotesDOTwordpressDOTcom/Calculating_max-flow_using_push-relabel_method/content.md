~~~~ 
title: Calculating max-flow using push-relabel method
type: post
status: publish
id: 922
tag: Combinatorics
tag: Maximum flow problem
category: Algorithms
category: Graph Theory
~~~~

Calculating maximum flow in a flow-network is a fundamental problem. It
has been observed that smart implementation of 'push-relabel' methods
performs better than algorithms based on finding 'augmenting paths'. We
have implemented one such variation of push-relabel method. It is known
as 'relabel to front' algorithm. It is discussed in details in
'Introduction to algorithms' by 'Cormen, Leiserson, Rivest, and Stein'.
We do not guarantee that it is the exact implementation of what is given
in this book. In fact, it is slightly different for we are selecting
nodes in some fixed order. We uses `boost::graph` library. Details are
in 'Readme.md' file. It is available on my [github
repository](http://github.com/dilawar/algorithms/tree/master/Push_relabel).
You can use it, but you are not allowed to modify it without notifying
the author. I wish to keep track of bugs.
