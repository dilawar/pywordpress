~~~~ 
title: Notes on boost::graph library 
type: post
status: publish
id: 909
tag: BGL
tag: Boost graph library
category: Library
~~~~

-   Copying a graph with a million-nodes took approx 2.13 seconds on 4gb
    RAM, i3 processor, desktop.
-   Creating and copying a graph with 10 million nodes failed with
    memory allocation error.
-   Replacing vector with deque made topologicalSort function faster
    (0.13 seconds Vs 0.03 seconds). It is now comparable to boost
    inbuilt topological_sort (0.01 seconds) on graph with 10k nodes.
-   
