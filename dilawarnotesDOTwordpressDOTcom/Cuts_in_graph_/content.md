~~~~ 
title: Cuts in graph 
type: post
status: draft
id: 935
category: Uncategorized
~~~~

A graph is a collection of nodes and edges. Various names are given to
graphs depending on their properties. Names are also given to graphs
according to the nature of edges and nodes of graph. An edge's endpoints
are nodes : if both end-points are same then an edge is called
self-loop; when an edge has more than two distinct end-points it is
called hyper-edge; otherwise it is the 'usual edge'. A graph with
hyper-edge is called hyper-graph. Another way of looking at hyper-graphs
is to visualize each node in graph as a hyper-node. A hyper-node is a
collection of nodes and  end-points of an edge in hyper-graph are
hyper-nodes. It is not always easy to visualize hyper-graphs when we see
an edge having more than two end-points.\
\
When we remove some edges from a graph, we find that sometimes graph is
broken into components : there is no connection between two components
of a graph. Such set of edge which when removed breaks the graph into
k-components is called k-cut. If a k-cut breaks the graph into 2
components, it is called 2-cut. This is the usually cut we see in the
network-theory. If we can prove that such a set of edges which when
removed from graph breaks it into k-components is minimal, we say that
it is a minimal cut.\
\
  Some nodes in graph has special property. For instance, a node may not
have any incoming edge or outgoing edge. A node with no outgoing edge is
called terminal. If we break the graph into components such that each
terminal node is in separate component, then such a  cut is called
'multi-way cut'.

 

 
