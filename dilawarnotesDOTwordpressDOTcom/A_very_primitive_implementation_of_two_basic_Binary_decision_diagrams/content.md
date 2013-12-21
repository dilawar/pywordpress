~~~~ 
title: A very primitive implementation of two basic Binary decision diagrams
type: post
status: publish
id: 464
tag: Binary decision diagrams
tag: c implementation of BDD
category: Algorithms
category: Programming
category: VLSI
~~~~

Binary decision diagrams are awesome. Read about them. Knuth has written
about them. You should be able to locate some material on the net. In a
nutshell, BDD is a way to represent a Boolean function uniquely. Now
lets talk about this primitive implementation. We have an array called
'mem' which keeps all the nodes of a BDD. In each BDD, there are two
sink nodes which are fixed at the bottom of an array 'mem' which keeps
all of our bdd-nodes. These two nodes, sink0 and sink1 are the last
nodes in a BDD to which all other nodes must have a path. All nodes in
any BDD must be unique, in a sense that no two nodes in a BDD should
have equal triple value of (tag, lo, hi). A data-structure called
'bddNode' has been type-defined which has four fields. These are tag,
index, lo, hi (actually there is a fifth one also which we are not
using). The field, tag, is the number of nodes in a particular BDD;
index, is the variable index; lo, is the address of its LO node; and hi,
is the address of HI node. Field 'tag' is used for making debugging
easier. THIS IS NOT THE MOST EFFICIENT DATA-STRUCTURE. We are
constructing two already reduced BDDs. First is  \$latex bdd1 = x\_1 +
x\_3\$ and second one is \$latex bdd2 = x\_2 \\oplus x\_3\$. Since there
are only two variables in each bdd, the question of ordering does not
arise. However these two functions are defined over 3 variables,
[![x\_1, x\_2,
x\_3](http://moodle.iitb.ac.in/filter/tex/pix.php/6ae787bde8f16f207b980a80e99115e6.png "x_1, x_2, x_3")](http://moodle.iitb.ac.in/filter/tex/displaytex.php?x_1%2C+x_2%2C+x_3 "TeX").
On these line, many primitive BDD's can be built over a collection of
variables. Since file was getting too longer to understand, I have not
coded how to compose two bdd's such as \$latex bdd3 = bdd1 \\& bdd2\$
etc.. One can write a generic function to do this. HINT : Think of a BDD
node as an if-then-else structure e.g. if variable 3 then goto node 2
else sink0. A simple printNode function is provided. It will print a
single BDD node. It would be good if you can write printBDD function
which can print a full BDD. HINT : Graph traversal. Great many things
can be done with/on BDD's. Have fun. [sourcecode language="cpp"] /\* \*
=====================================================================================
\* \*       Filename:  demo\_bdd.c \* \*    Description:  A demo program
to show how operations on BDD are \*    implemented. \* \*       
Version:  1.0 \*        Created:  Thursday 18 August 2011 01:15:29  IST
\*       Revision:  none \*       Compiler:  gcc \* \*         Author: 
Dilawar Singh (Graduate Student, EE IITB), dilawar@ee.iitb.ac.in \*     
Institute:  IIT Bombay \* \*
=====================================================================================
\*/ \#include    \<stdio.h\> \#include    \<stdlib.h\> \#include  
 \<string.h\> /\*  for length function. \*/ \#define addr\_(a)
(addr)(size\_t)(a) typedef unsigned int addr; int totalNodes = 0; /\*
this many nodes are currently in use. \*/ typedef struct node { unsigned
int \*tag; /\* Useful in debugging.\*/ addr lo; addr hi; unsigned int
index; int vRef; /\*  reference count minus 1. NOT USING. \*/ } bddNode;
int i; void printNode(bddNode\*); void printBdd(bddNode\*); bddNode\*
constructBdd(char\* fVar[], char\* var[], char\* binOp); bddNode
mem[100]; /\* \*  These sink-nodes never change. Let's define them and
we'll put them in 'mem' at bottom. There, \*  they will rest in peace
all the time. \*/ bddNode\* sink0; bddNode\* sink1; int main() { /\* 
Let's define variables with ordering. There are algorithms available to
\*  find a suitable ordering such that BDD size is minimum. For now, we
\*  assume that ordering is know to us \*/ /\*  for simplicity sake,
char 1 means x\_1 and so on. \*/ char \*var[] = {"1", "2", "3"}; /\* 
Note that these are char and not numbers. \*/ /\*  Now we should have
some binary operations. What is a use of BDDs if we \*  can not compose
them. \*/ char \*binOp[] = {"&", "|", "\^", "\$", "\#"}; /\* I am not
using all of them.  \*/ /\*  now we need to construct some bdd so that
we can have some fun! Ideally, \*  there should be a function to which
we can pass a boolean function and \*  presto, we get a bdd. Why don't
you do that and I hardcode two BDD's.\*/ /\*  I am hardcoding two bdds,
bdd1 and bdd2. Later we will combine them \*  using a binary operation
and produce a new BDD. \* \* let bdd1 = x\_1 | x\_3, read x\_1 'or'
x\_3. \* NOTE : Sink nods are labelled as 000 (0) and 011. DO NOT
CONFUSE THEM \* WITH OTHER NODE LEVELS which are variable names. \*
\*              1 \*             / \\ \*           LO   \\ \*          
/     HI \*          3       \\ \*        /  \\      011 \*       LO  
HI \*      /      \\ \*    000      011 \*/ /\*  initialize sink nodes
and put them at the bottom of mem\*/ sink0 = mem; sink1 = mem + 1;
totalNodes += 2; /\*  two sink nodes. \*/ sink0-\>tag = 0; sink0-\>index
= 0; sink0-\>lo = 0; sink0-\>hi = 0; sink1-\>tag = 1; sink1-\>index = 0;
sink1-\>lo = 1; sink1-\>hi = 1; /\*  let's construct bdd1 \*/ char\*
var1[] = {"1", "3"}; /\*  these are variables bdd needs. \*/ bddNode\*
bdd1 = constructBdd(var1, var, "&"); /\*  and now bdd2 which is x\_2 xor
x\_3 \* \*            2 \*         /    \\ \*        LO      HI \*      
/         \\ \*      3           3 \*     / \\         / \\ \*    LO 
HI     HI  LO \*     |    \\   /    / \*     |     \\/     / \*     
\\   /  \\   / \*       000    011 \* \*/ char\* var2[] = {"2", "3"};
bddNode\* bdd2 = constructBdd(var2, var, "\^"); return 0; } void
printNode(bddNode\* p) { printf("Node : "); printf(" (tag(%d),
index(%x), lo(%x), hi(%x))\\n", p-\>tag, p-\>index, addr\_(p-\>lo),
addr\_(p-\>hi)); } void printBdd(bddNode\* p) { } bddNode\*
constructBdd(char\* fVar[], char\* var[], char\* binOp) { if
(strncmp(binOp, "&", 1) == 0) { int nodeInThisBDD = 0; printf("Building
a BDD with AND operation\\n"); bddNode\* r = mem + totalNodes + 1;
nodeInThisBDD++; totalNodes++; bddNode\* rl = mem + totalNodes + 1;
nodeInThisBDD++; totalNodes++; nodeInThisBDD += 2; /\*  two sink nodes.
\*/ r-\>tag = nodeInThisBDD; r-\>index = (\*fVar[0] - 48) ; r-\>lo =
addr\_(rl); r-\>hi = addr\_(sink1); rl-\>tag = --nodeInThisBDD;
rl-\>index = (\*fVar[1] - 48); rl-\>lo = addr\_(sink0); rl-\>hi =
addr\_(sink1); printNode(r); printNode(rl); return r; } if
(strncmp(binOp, "\^", 1) == 0) { int nodeInThisBDD = 0; printf("Building
a BDD with XOR operation.\\n"); bddNode\* r = mem + totalNodes + 1;
nodeInThisBDD++;  totalNodes++; bddNode\* rl = mem + totalNodes + 1;
nodeInThisBDD++; totalNodes++; bddNode\* rh = mem + totalNodes + 1;
nodeInThisBDD++; totalNodes++; nodeInThisBDD += 2; /\*  two sink nodes
\*/ /\*  name it \*/ r-\>tag = nodeInThisBDD; r-\>index = (\*fVar[0] -
48); r-\>lo = addr\_(rl); r-\>hi = addr\_(rh); rl-\>tag = nodeInThisBDD
-1 ; rh-\>tag = nodeInThisBDD - 2; rl-\>index = rh-\>index = \*fVar[1] -
48; rl-\>lo = rh-\>hi = sink0; rl-\>hi = rh-\>lo = sink1; printNode(r);
return r; } else { fprintf(stderr, "This operation is not implemented
yet."); } } [/sourcecode]
