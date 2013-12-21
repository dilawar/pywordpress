~~~~ 
title: VLSI Verification - Some notes on Present and Future
type: post
status: publish
id: 304
tag: review of verification of vlsi
tag: verification of vlsi
tag: vlsi
category: VLSI
~~~~

[caption id="" align="aligncenter" width="480" caption="From
http://shemesh.larc.nasa.gov/images/humor-sneak-a-peek.jpg"][![](http://shemesh.larc.nasa.gov/images/humor-sneak-a-peek.jpg "From http://shemesh.larc.nasa.gov/images/humor-sneak-a-peek.jpg")](http://shemesh.larc.nasa.gov/images/humor-sneak-a-peek.jpg)[/caption]
When hardware and software grows in size, they create a lot of pain in
ass of the developers and users alike. Frankly, most of these
improvement are not necessary e.g. the behemoth Microsoft Word which is
good for nothing. If a console application is doing my job effectively,
why would I add so much of crap known as Graphical User Interface. But
there are few areas where increase in size, mostly translate into
effectiveness and improvement. Hardcore VLSI is one of that area. When
one builds a large system, first thing one asks oneself, is it correct?
Well first one has to write it down clearly. These written description
are **specification**. Even if the probability of occurrence of an error
in design is 1 in a million still you'll get hundreds of them in a
modern VLSI system. And any of these errors can throw you out of
business. Verification and testing takes more than 60-70% of all the
effort required to realise a VLSI design in practise these days. So you
should make sure to hire careful and geeky people like me. And instead
of wasting money on buying licenses of costly softwares, you can give me
50% of that. Its like why would you pay \$1000 to hire someone with a
fancy automated weapon when Zedi Knight can do the same thing with light
saber in 10% of that cost. But since managers are mostly dumb, he cost
becomes so high that only few new designs are coming out of industries.
Industries are spineless and they have not explored the possibilities
how much university can offer if they show a little bit of backbone.
Academia on the other hand, sometime solely driven by curiosity only,
have produced some methods which are now hijacked by industries for
their own benefits. Anyway, now we get to the core of our topic.
Simulation will not work in future! That much I am sure of. You just can
not simulate all the possible combination described specification in a
modern day VLSI design. Even if you have 1000 of computers at your
disposal. It would be foolhardy to do so. However, simulation with
formal methods may yields wonderful results. We concentrate on the
formal methods here. Any improvement in these methods will be of great
values for VLSI verification. [Reduced Binary decision
diagrams](http://en.wikipedia.org/wiki/Binary_decision_diagram) (RBDD)
and [Kripke Structures](http://en.wikipedia.org/wiki/Kripke_structure)
are very prominent tools these days. [In the
past](http://www.springerlink.com/content/j335v4472745r366/), the use of
formal methods in practise seemed hopeless and hence only few crazy
people stuck to those. Recently, as my professor Madhav P Desai lectures
implies, industries are  trying out formal verification like Z notation
to document a system properties more rigorously. Model checking and
theorem proving (on certain structures) a[re being plugged
in](https://docs.google.com/viewer?url=http://www.cl.cam.ac.uk/~jrh13/slides/types-04sep99/slides1.pdf)
to complement more traditional one of simulation. Before one starts
verifying, one needs to write down the specification of the system
clearly. Talking in terms of states are probably the most ubiquitous
these days. A state machine is formed and described in some Hardware
Description Language like in my favorite VHDL then one can proceed to
simulation and all. Specification need not be written in standard way.
The emphasis should be on the clarity of the system. Two well
established approach to verification are model checking and theorem
proving. Model checking is very fast but can handle finite states.
Theorem proving can handle infinite state space. In model checking, one
builds a finite model of a system and check that a desired property
holds in that system. This is done by search exhaustively (and some
times wisely), if it does not hold and a counterexample is produced.
That is its greatest strength to able to produce and error and thus
suitable for debugging. Since model is finite, it will terminate. It is
mostly used in hardware and protocol verification. Two approaches are
genrally used in model checking, TEMPORAL MODEL CHECKING and '**find and
automation and compare to the specification to determine whether or not
its behaviour conforms to that specification**'. For example, Language
Inclusion (Har'El and Krushan, 19941], refinement ordering [Cleaveland
et all. 93], observal equivalence [Cleaveland et all 93, Fernandez, 96,
Roy and de Simone 90]. Vardi and Wolper [1986] have shown how the
temporal model checking problem could be recast in terms of automata,
thus relating two approaches. Model checking is much faster than theorem
proving. But the problem is STATE EXPLOSION. There are heuristics to
improve this though [Krushan 1994; Krushan 1994] and semantic
minimization (Elseaidy et al. 1996] to eliminate unnecessary states from
a system modeling. Using this method one has verified 10\^120 reachable
states. Theorem proving can deal with infinite state space. It uses
structural induction to prove over infinite domains. The overreaching
goal of formal methods is to help engineers construct more reliable
systems. Decomposition of  a larger set into smaller sets will always be
beneficial. A global property is broken into local properties which are
conceptually easier to handle. Abstraction is also needed, for example,
hardware specification  can written down in more abstract language like
esteral. Combination of mathematical theories is also a very less
explored area. One solid concepts from one discipline can  find
application in another numerous fields, graph theory is one of the most
remarkable example of it. And finally, who can forget to include better
data structures and algorithms. One can get more ambitious. rather than
building models for some specific problem, one can romanticise
"meta-tools" which themselves can produce or change themselves to handle
a particular problem domain. Integration of available methods will also 
help. RESOURCES [1]
[http://formalmethods.wikia.com/wiki/Formal\_Methods\_Wiki](http://formalmethods.wikia.com/wiki/Formal_Methods_Wiki)
[2]
[http://shemesh.larc.nasa.gov/fm/index.html](http://shemesh.larc.nasa.gov/fm/index.html)
[3] [Model checking at
CMU.](//www-2.cs.cmu.edu/~modelcheck/pubs.htm#online)fa
