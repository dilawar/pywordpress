~~~~ 
title: Lobbying for Haskell 
type: post
status: publish
id: 938
tag: Haskell
tag: programming
category: Haskell
category: Language
~~~~

> ... but one must not be surprised if outsiders don't take Haskell too
> seriously... [We] say a lot about what functional programming isn't:
> It has no assignment, no side effect, no flow of control but not much
> about what it is. The functional programmer sounds rather a medieval
> monk, denying himself the pleasures of life in hope that it will make
> him virtuous. To those interested in material benefits, these
> 'advantages' are totally unconvincing.

-- "Why functional programming matters"

John Hughes, The Computer Journal, 1989

If someone comes to you with a new programming language, it is the time
to run in the other direction. Who needs one more language; don't we
have millions of them already? Besides, if I can do something in a
language I know well with the help of libraries, should I invest my time
in learning a new language? A young student does not have such worldly
concerns. He can be easily excited about a new language. Why functional
programming language? And why Haskell? Computer science people have
their own reasons on why they prefer one language over other. But what
about others, especially Electrical Engineering people, who can be
equally, and often are, equally concerned about languages. Electrical
engineers are usually deals with hardware and the way things gets
executed on it. They prefer C/C++ to explore their hardware and
rightfully so. I doubt if any language can beat it on 'fetch and
execute' type of processors (except for assembly). There is also
designing and modeling side of electrical engineering. Here we have
HDLs, and some other languages. Python is a versatile language designed
for convenience: no seg-faults and core dumps. Moving from C to Python
is relatively easy. Both languages have same type of flow. C/C++ is
often taught in all engineering branches; python can be learned with
little effort. Its an incredibly good combination. In functional
programming languages, most if not all things are functions. A function
takes functions as argument and return a function as result. In C/C++,
to do this, you have to use function pointers imaginatively. It's a
loose definition which might irritate those who have a theoretically
neat mind. Nonetheless, it will serve our purpose for this informal
discussion. It's the ease with which we can 'glue' functions together to
create a new function which makes functional programming attractive. You
can go through a classic work, 'Structure and Interpretation of Computer
Programs' to get the taste of functional programming. They have used
Scheme, a dialect of Lisp language which is a functional programming
language, old as Fortran. Moving from Lisp or Scheme to Haskell is
rather simple. But learning Haskell can be challenging for those who are
from C world. Many of them usually give up when they are confronted with
monad. We can list out some benefits of Haskell over C/C++. The cost is
speed and memory. I am not suggesting that Haskell is always slow. It
can be very fast, and sometimes as fast as C. Both Python and Haskell
drops into C to do computationally expensive tasks. While there is
little you can do in pure Python to make things faster, Haskell provides
many opportunities for optimization at its back-end. Learning to
optimize the Haskell code can be challenging. A lot of work has been
done on these directions. The beauty of Haskell (or any functional
programming language) lies in that fact that it captures the idea of
recursion most naturally. Once you know the syntax, writing recursive
functions are extremely easy. This is usually their selling point:
recursive functions and recursive data-structures are easier to handle.
Python has also borrowed some of these functional programming features
such as list-comprehension and lambda functions (anonymous function).
The C++ 2011 standard has Lambda function. That should be the proof
enough of its syntactic beauty. The core of Haskell is small. If lambda
calculus -- which is Turning complete -- has only two operations and can
model any computation then why should core of any language have more?
Clean syntax and a small core are beneficial for those who infer the
logic by looking at the program. Translation of Haskell code to
something else should be easier. Moreover as parallel hardwares are
becoming common-place, functional languages will increase in their
stature. Figuring out parallel component in C/C++ is not easy.
Programmer has to figure it out and code it by himself. People have
found that it is relatively much easier for Haskell compiler to figure
the parallelism out by itself. If you have ever written a large program
(say a thousand line of code) then you must have spent more time
debugging the application than coding it. In fact, a saying in
programming community goes, 'Anyone can code, it takes a programmer to
debug'. Haskell reduces chances of a programmer creating bugs
significantly by its strong type system. In Electrical Engineering, no
one really gives a damn if a language has strong type-system. Who cares
if VHDL have a stronger type-system than Verilog? You should ask your CS
friend about it and its merit. A simple example might throw some light
on it.

typedef speed\_t double; typedef acceleration\_t double; typedef
distance\_t double; speed\_t a =10.0; acceleration\_t b =9.8;
distance\_t c = a + b;

Now it is illegal to add speed and acceleration. But it is a legal piece
of code in C. Such bugs will be incredibly hard to locate in C. An
equivalent code in Haskell would not compile at all. The operator '+'
demands that a and b should be of same type which they are not. Since
Haskell check types at compile type (unlike python which checks it at
run-time), it will easily catch it (and can easily irritate you). People
talk about many other benefits Haskell provides to a programmer. One of
them is that one has to type fewer lines. This is certainly true but
what is doubtful if producing n line of code in Haskell is less time
consuming that writing its equivalent in Python. My own experience with
Haskell language are of mixed kind.  When you are working with recursive
stuff, Haskell is very pleasant to code in. When it comes to
non-recursive stuff such as graph, Haskell can become painfully slow. It
has to convert graph (which is a non-recursive data-structure) to an
equivalent recursive structure which takes a lot of memory. You will
overflow your stack more often in Haskell than in Python or C. Hardcore
algorithmic people who deals with large graphs will not find it very
exciting. I'd recommend Haskell not because you are going to use to use
it in your professional life. Most probably you won't. It would be a
worthy investment just to learn the most rudimentary Haskell. Haskell
makes you think and reason at very high level. Mistakes made at high
levels become easily apparent in Haskell then they would be in C or
Python. Moreover, once you have become efficient in Haskell, breaking
your design in smaller pieces and gluing them together will come
naturally to you. If writing modular program is a virtue than Haskell is
perhaps one of the best language around. Breaking and gluing functions
is the essence of of functional programming; it is made easier in
Haskell. Learning Haskell will make you a better programmer even if you
are not coding in Haskell. You can also try Scheme. Best thing about
Scheme is that you can call yourself a 'schemer' who schemes everyday,
which is million times cooler than calling yourself a 'Haskeller'.
Resources : [1] Prof. Sanyal [page on
Haskell](http://www.cse.iitb.ac.in/%7Eas/fpcourse/fpcourse.html). Check
out the problem sheet. [2] [Real world
Haskell](http://book.realworldhaskell.org/read/). This is a really good
book to start with. [3]
[http://learnyouahaskell.com/](http://learnyouahaskell.com/) . Read it
at your own risk. Sometimes he says much about nothing. [4] Structure
and interpretation of computer program. This old classic is freely
available. Still a great book to learn about computer programs. --
Dilawar EE, IITB

###### Related articles {.zemanta-related-title style="font-size:1em;"}

-   [Haskell - Mind
    Blowing](http://drtallman.wordpress.com/2013/06/19/haskell-mind-blowing/)
    (drtallman.wordpress.com)

