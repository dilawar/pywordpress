~~~~ 
title: Declarative languages and biological systems 
type: post
status: publish
id: 970
category: Modelling
~~~~

A program written in declarative paradigm does not specify "how to do
it" (like we do in C, Python etc.), it only contains statements which at
best tell the computer "what to do". The spice netlist is one such
example, here we  tell ngspice or some other spice, what to compute
(like .OP, .DC, .AC etc.). To be sure, these distinction are rather
based on arguments which are nothing but "hand-waving", but too many
people use these terms to ignore them. For example, FIFO (First In First
Out) is an algorithm, but people often use it as if it is an object
(Queue). There is no thick-line which strictly separates languages
according to these categories. Following example which computes
factorial can be classified  "somewhat declarative" (written in
functional programming language haskell). Here, we are not exactly
saying how to "really" compute a factorial of a natural number. [code
language="erlang"] fact 0 = 0 fact 1 = 1 fact n = n \* fact (n -1)
[/code] Following will not be called declarative at all. [code
language="C"] unsigned long factorial(unsigned n) if(n == 0) return 0;
if(n == 1) return 1; unsigned long result n; for(unsigned i = n-1; i \>
0; i--)     result \*= i; return result; [/code] (None of these snippets
is tested). I am not sure if to be "declarative", a program must lack
 control flow or there is a consistent theoretical category into which a
program must fit. Till people with neat theoretical mind fix the
confusion for us, we can look at the uses of this paradigm. There are
many and quick search will reveal some. Let me share one on which
currently I have to work (not enjoying it too much) i.e. modeling large
scale neural networks. A VLSI engineer is trained not to be frightened
with numbers of components. But unlike CMOS devices, two neurons even
when they belong to same class much like two humans, do not behave in
the same way. Fortunately their behaviour is not without a pattern, so
attempts are being made to model them (as a real biological network) for
a computer to answer few questions. Already much work has been done in
the area of classifying neurons and finding equivalent "electrical
models" of them; they have been simulated independently and sometimes as
a group of few. These models were saved in some format and there are now
many such formats. Efforts are on way to standardize them. It is agreed
in general that some declarative paradigm will be most suitable for
Biologists might not prefer to learn a language to tell the computer
"how to do it", they would rather concentrate on "what to do". Neither
it is expected from them. Engineers find it hard to learn a second
language. Many avoid going thoroughly the first one. Astronomers have
been using HDF5 format to store complex data (hierarchical patterns).
Now there is XML technology all around. XML looks dirty to human eyes
but a computer can easily read them. So why not describe "what to do" in
XML. Imagine, rewriting a ngspice script in XML format and what they
wish to do will be clear. The major difference however remains, two
neurons belonging to same class do not behave like two capacitor or two
transistors.  Much depends on how they are connected and who is around
them doing what; and what is happening at different scales. A release of
certain chemicals or presence of certain ions can not only change the
values of component in equivalent circuit model, it can also change the
circuit model itself. The speed of computation depends mainly on how
fast you can solve electrical circuits. But there is concernt whether a
"jack of all trade" simulator is sufficient. Multiscale modelling, as it
is called these days, is found to capture biological systems. How
changes in "one scale"changes the behaviour at different scale? This is
answered by experimentalists. They also prepare models to capture the
behaviour. And how to describe it is usually done by, well, programmers.
Now the problem, is how to describe a model for multiscale-modellings;
if not using some data-base (XML)? To me, it looks like more of
sociology of neurons than computation of networks. There is a lot of
scope of hand-waving and null-hypothesises; and along with it, as
usually the case in these professions, much scope for personal
ingenuity. I prefer my boring subjects where step by step reasoning
using well-established tricks yield results about an idea. Some people
have used Erlang to model "brain" given its capacity to easily launch
millions of threads. Each neuron is encoded in a process and one can
launch as many as one wants. Messages among these processes represents
changing environment and what one neuron is sending to other.
Theoretically, its is pretty neat. The principle of reality appears to
ruin the party: how to crunch numbers as soon as next update is
available? One can also simulate them as VLSI models are simulated using
HDL but that will be incredibly slow. Erlang is not reputed to be a
number-crunching language. But there is scope here for at least
modelling very simple "spike models" or "integrate and fire model" but I
am not aware if anything has been done on these lines. Availability of
many-core hardware on which one can launch many threads will solve many
problems. But again since the behaviour of two neurons is not same, you
can not model them which might put you in a position where you use
embarrassingly parallelism available as "single instruction" working on
"multiple data".  Besides that would not be research, that is just
development, no matter how important it is. Those who are more
interested in how biological systems are modelled in multi-scale ways
can look-up this entry from the lab for last year google summer of code.
GSoC is co-ordinated by INCF India node.
[http://www.incf.org/programs/training-committee/gsoc](http://www.incf.org/programs/training-committee/gsoc)
-- Dilawar
