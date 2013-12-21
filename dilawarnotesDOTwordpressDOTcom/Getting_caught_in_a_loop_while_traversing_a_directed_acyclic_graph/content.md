~~~~ 
title: Getting caught in a loop while traversing a (directed acyclic) graph
type: post
status: publish
id: 692
tag: Boost C++ Libraries
tag: boost regex
tag: loop in graph
tag: Regular expression
category: Algorithms
category: Graph Theory
~~~~

How to detect if you are getting caught inside a loop when you are
traversing a directed graph. This is equivalent of checking if you graph
is a [Directed Acyclic
Graph](http://en.wikipedia.org/wiki/Directed_acyclic_graph "Directed acyclic graph")
(DAG). Assume that each vertex of graph has a label such as A, B, C,
etc. While you are traversing the graph, you keep your labels of
traversed vertices on a stack or in a vector. If you construct a string
out of this traversal, you will get a pattern like the following one.

     A,B,D,E,F,D,E,F,D,E,F

Whenever you are caught in a loop, a path will repeat itself. We have
`D,E,F` repeating itself. Now there are two ways to detect this. One is
a classical graph based method which is efficient \$latex O(E+V)\$. The
second one, about which I am going to talk about now, is not as
efficient as first but but it is very easy to code. It is based on
[regular
expressions](http://en.wikipedia.org/wiki/Regular_expression "Regular expression").
All we have to do is  construct a string out of the data-structure which
holds the vertex traversal order and match it against a regular-pattern
which looks for the repeated substrings. Here is one such pattern
written using boost regex library.

     boost::regex rx ("^([0-9a-zA-Z_@]+,)+(?[0-9a-zA-Z@_,]+)(g{cycle})$", boost::regex::perl);

Care has to be taken while using this regex. First, I have special
character `@` in the label of vertex. And this pattern assumes that if
there is a single repetition such as `A,B,A,B` or `A,B,B` etc, then it
must lead to a loop. In my case it is justified. You should think if
this is the behavior you want. And again, it is not as efficient as
standard graph algorithms to detect loop (which uses [Depth First
Search](http://en.wikipedia.org/wiki/Depth-first_search "Depth-first search")).
But for writing quick tests, it is a good approach. I have used boost
regex library. I am already using boost graph library therefore I need
not look for other libraries. I have heard a some good things about
GNU-regex library but have never used myself. Also, my gcc (4.6) does
not support 2011C++ fully e.g. regex is not implemented fully. Have a
look at its status page before writing any regex using ` ` header
\<regex\>. -- Dilawar

###### Related articles {.zemanta-related-title style="font-size:1em;"}

-   [Computer Algorithms: Topological Sort
    Revisited](http://www.stoimen.com/blog/2012/12/10/computer-algorithms-topological-sort-revisited/)
    (stoimen.com)
-   [Find the Simple Cycles in a Directed
    Graph](http://cs.stackexchange.com/questions/7216/find-the-simple-cycles-in-a-directed-graph)
    (cs.stackexchange.com)

