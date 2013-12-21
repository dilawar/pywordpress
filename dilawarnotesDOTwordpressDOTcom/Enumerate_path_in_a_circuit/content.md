~~~~ 
title: Enumerate path in a circuit
type: post
status: publish
id: 220
tag: depth first search
tag: dot
tag: graph theory
tag: graphviz
tag: path delay
tag: verification
tag: vlsi
category: Electrical Network
category: Graph Theory
category: Programming
category: Technology and Engineering
category: VLSI
~~~~

Consider the following circuit and its directed graph. Directed graphs
can represent many things. In our case though, it represent a digital
circuit as shown below. Consider each node of the graph as a logical
gate of the circuit. The incoming edges are input to the logic gate and
outgoing edges are the output of the logic gate. [caption
id="attachment\_224" align="aligncenter" width="663" caption="Circuit is
drawn in Qucs simulator which I think will be of great value in near
future."][![](http://dilawarnotes.files.wordpress.com/2010/10/assign4.png?w=1024 "A digital Circuit ")](http://dilawarnotes.files.wordpress.com/2010/10/assign4.png)[/caption]

Following figure shows its directed graph. Buffer Y9 and Y10 are ignored
since they were inserted to distinguish u\_1 from p\_00 etc. Now if we
need to test this circuit for path delays, we need to enumerate the path
firsts. After converting the circuit into a graph, enumeration the path
is a routine problem and can be solved by using **Depth First Search**
algorithm. An *edge* from one node to other shows that a *wire* exists
between them. By *path* we mean this *wire* only.

The path is shown below. **dot** Tool is used to generate this graph.
Now the problem is reduced to enumerating the path between input and
output.﻿ This can be done using the standard **Depth First Search
(DFS).**The procedure is following. [caption id="attachment\_223"
align="alignleft" width="218" caption="Figure representing a digital
circuit."][![](http://dilawarnotes.files.wordpress.com/2010/10/graph1.png?w=218 "graph1")](http://dilawarnotes.files.wordpress.com/2010/10/graph1.png)[/caption]

-   **Partition the graph** We partition nodes of the given graph
    \$latex G(E,V)\$ in to two sets namely \$latex V\_{input}\$ and
    \$latex V\_{output}\$.
-   Clearly, \$latex  V\_{input} \\bigcup V\_{output} \\subset V\$. We
    may have a trivial case in which \$latex V\_{input} \\bigcup
    V\_{output} \\subseteq V\$. Clearly, the number of path in this
    situation is equal to the number of edges in \$latex G\$. In our
    problem we are already been provided with \$latex V\_{input} = \\{a
    , b\\} \$ and \$latex V\_{output} = \\{u\_1, u\_2, u\_3, u\_4\\}\$.
-   **Step 1** Start from a node \$latex V\_i \\in V\_{input}\$. Mark
    this node as*used*. Initialize counter to 0. Initialize stack to
    keep track of path.
-   **Step 2** Pick an edge and reach to the next connected node. Push
    this edge on the stack. Do it till you hit a node which belongs to
    \$latex V\_{output}\$. Increase counter by 1.
-   **Step 3** Pop the stack and traceback your path. Do it till you
    meet a node which have an edge which has not been pushed on to the
    stack. When you get this node. Repeat step 2. Else go to step 4.
-   **Step 4** Counter will give you the number of path between input
    node \$latex V-i\$ and the output nodes. If there are nodes left in
    \$latex V\_{input}\$, go to step 1. Else go to step 5.
-   **Step 5** Each input node have a counter value. Add them up. This
    gives the total number of path in the circuit.﻿ ﻿

Now these steps can be visualized easily. We start from node **a**and
traverse this graph. [caption id="attachment\_227" align="aligncenter"
width="592" caption="Start from a and enumerate all the paths ending at
the nodes starting with u. We have total of 6 paths. As we hit an dead
end, we increase the number of path by one. The numerics displayed at
the end of node represent this only. Edges with label 0 shows that this
is the first path we have taken. For examplem a-\>w-\>p00-\>u1 is one
path. We push these nodes on a stack. We increase the path number as we
hit u1 since it belongs to the end point. From here we trace back to
hunt down the rest of the paths which are shown by blue edges. This
trace-backing is most naturally implemented using stack. Any node name
prefixed with p\_  represents pop operation on the stack. Here, from u1
we got to p\_u1 which mean that pop u1. We reach p00 and we know that
there is one edge we have not traversed since it was not in the stack.
Now p00-\>u2 is one more path and we increase the path by one (path = 2
now). We traceback through p\_u2-\>p\_p01-\>p-w (pop u2, p01, and w) and
reach a to find a new edge p11 to be traversed. So on and so forth, we
enumerate all the paths. We should label every edge with label
path\_value so that we can keep track of the
paths."][![](http://dilawarnotes.files.wordpress.com/2010/10/path11.png "path1")](http://dilawarnotes.files.wordpress.com/2010/10/path11.png)[/caption]
In the same way, we can enumerate all the paths from input node **b**to
the output nodes.

 

[caption id="attachment\_228" align="aligncenter" width="615"
caption="Path from node b to output. The procedure is explained in the
previous figure. Here also we get 6
paths."][![](http://dilawarnotes.files.wordpress.com/2010/10/path2.png "path2")](http://dilawarnotes.files.wordpress.com/2010/10/path2.png)[/caption]

Well, we used graphviz to generate these graphs. We give these scripts.

 

[sourcecode language="css"] &lt;p style=&quot;text-align:
left;&quot;&gt;digraph G { node[fontzise = 10, width="0.4", height =
"0.4", margin = 0]; edge[color=red] subgraph cluster001{ style = filled;
color = lightgrey; node [style= filled, color=white] start [shape =
box]; start -\> a [penwidth = 4, headlabel = 0]; a -&gt; w [label = 0];
w -\> p00 [label = 0]; p00 -\> u1[label = 0, headlabel="1"]; p00 -\> u2
[headlabel="2"]; w -\> p01; p01 -\> u3[headlabel = 3]; a -\> p11; p11
-\> u2 [headlabel =4]; p11 -\> u4 [headlabel = 5]; a -\> p10; p10 -\> u3
[headlabel = 6]; } subgraph cluster002{ style=filled; color=pink; edge
[color = blue] u1 -\> p\_u1; //p\_u1 -&gt; p\_p00; p\_u1 -\> p00; u2 -\>
p\_u2; p\_u2 -\> p\_p00; p\_p00 -\> w; /// u3 -\> p\_u3; p\_u3 -\>
p\_p01; p\_p01 -\> p\_w; p\_w -&gt; a; // // u4 -\> p\_u4; p\_u4 -\>
p\_p11; p\_p11 -\> a; // } subgraph cluster004{ style=filled;
color=pink; edge [color = blue] u3 -\> p\_u3\_; p\_u3\_ -&gt; p\_p10\_;
p\_p10\_ -\> a [headlabel = "END"]; u2 -\> p\_u2\_; p\_u2\_ -\> p11; }
subgraph cluster004{ p00; p01; p11; p10; } subgraph cluster03{ style =
filled; color = lightgrey; node [style= filled, color=white] u1; u2; u3;
u4; } } [/sourcecode] [sourcecode language="css"] digraph G {
node[fontzise = 10, width="0.4", height = "0.4", margin = 0];
edge[color=red] subgraph cluster001{ style = filled; color = lightgrey;
node [style= filled, color=white] start [shape = box]; start -\> b
[penwidth = 4, headlabel = 0]; b -\> x [label = 0]; x -\> p00 [label =
0]; p00 -\> u1[label = 0, headlabel="1"]; // pop p00 -\> u2
[headlabel="2"];// pop x -\> p10; p10 -\> u3[headlabel = 3]; // pop b
-\> p01; p01 -\> u3 [headlabel =4]; // pop b -\> p11; p11 -\> u2
[headlabel = 5]; // pop p11 -\> u4 [headlabel = 6]; // pop } subgraph
clusterPOP1{ style=filled; color=pink; edge [color = blue] u1 -\> p\_u1;
p\_u1 -\> p00;// Go forward. u2 -\> p\_u2; p\_u2 -\> p\_p00; p\_p00 -\>
x; // go forward. u3 -\> p\_p10; p\_p10 -\> p\_x; p\_x -\> b; // go
forward. u3 -\> p\_u3; p\_u3 -\> p\_p01; p\_p01 -\> b; // go forward. u4
-\> p\_u4; p\_u4 -\> p\_p11; p\_p11 -\> b [headlabel = "EXIT"]; }
subgraph clusterPOP2{ style=filled; color=pink; edge [color = blue] u2
-\> p\_u2\_; p\_u2\_ -\> p11; // go forward. } subgraph cluster03{ style
= filled; color = lightgrey; node [style= filled, color=blue] u1; u2;
u3; u4; } } [/sourcecode]
