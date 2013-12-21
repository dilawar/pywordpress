~~~~ 
title: Floating point Arithmetic Disasters 
type: post
status: publish
id: 429
tag: Floating point arithmetic disasters
category: HDL
category: History
category: Technology and Engineering
~~~~

**“ Floating point numbers are like piles of sand; every time you move
them around, you lose a little sand and pick up a little dirt. ”** —
Brian Kernighan and P. J. Plauger. If you are using windows machine then
open your calculator, try following calculation, \$latex \\sqrt[2]{4} -
2\$ and \$latex 2 - \\sqrt[2]{4}\$. Are both results same? Are they
equal to 0? After saying WTF 3-4 times, try contemplating the
consequences of it. 3 major accidents which happened in which floating
point errors were shoot off the accepted limits were quiet deadly.

-   **Ariane 5 rocket**. [June 4, 1996] 10 year, \$7 billion ESA project
    exploded after launch. They converted 64-bit float to 16 bit signed
    int. Unanticipated (that what they call it in their official report,
    it's simply insane) overflow.

See this interesting report
here [http://www.around.com/ariane.html](http://www.around.com/ariane.html)

-   **Vancouver stock exchange**. [November, 1983]. Index undervalued by
    44%. Recalculated index after each trade by adding change in price.
    22 months of accumulated truncation error.

Well, no one can blame people on Wall Streets. Screwing up the financial
world runs like plague in their family.

-   **Patriot missile accident**. [February 25, 1991] Failed to track
    scud; hit Army barracks, killed 28. Inaccuracy in measuring time in
    1/20 of a second since using 24 bit binary floating point.

I do not think any U.S. newspaper reported the incident since arms
industry lobby is very influential. Report is available
here [http://www.fas.org/spp/starwars/gao/im92026.htm](http://www.fas.org/spp/starwars/gao/im92026.htm)
If you have seen that Movie 'The Matrix 3' in which Neo meets the
Architect, read this conversation between them. Neo: **Why am I here?**
Architect: **Your life is the sum of a remainder of an unbalanced
equation inherent to the programming of the matrix. you are the
eventuallity of an anomaly which despite my sincerest efforts I have
been unable to eliminate from what is otherwise a harmony of
mathematical precision. While it remains a burden asciduously avoided it
is not unexpected, and thus not beyond a measure of control. Which has
led you inexorably....here** Make sense why the Architect is helpless?
\$latex \\sqrt[2](4) - 2 \$ is not zero because of the algorithm
implemented inside the ALU to calculate the square root of a number.
They use Taylor series based algo (Most primitive being Newton Raphson
method). See [details
here](http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Approximations_that_depend_on_IEEE_representation).
These 'floating point arithmatic' is a tricky business. Second hurdle is
calculating the roots of 'polynomial'. **It is well proven results
[Group Theory - Évariste Galois, 1938]that there exists no algorithm
which can produce the exact root of a polynomial of degree higher than
3.** One has to do the numerical computations. Avoid calculating roots
of polynomials as Plague whenever you see them in your scientific
computation. That is one reason why there is no state-space based
circuit simulator even though they are conceptually tempting. There are
languages which are capable of calculating these expression precisely.
They emulate 'Turing machines' (equivalent to Lambda calculus).
Languages such as LISP (which is popular among AI people) and the new
cult Haskell are capable of computing to the arbitrary number precision,
only bounded by the memory. The drawback is, that since every bit is
treated as a 'symbol', these languages are computationally very slow.
Supporter of these languages say, and I agree, that if you learn these
'functional programming languages, you will laugh at jokes which no one
will understand. Haskell is also being used as HDL and the verification
is quite easy in these languages. But functional languages are yet to
make their way into EE-IITB curriculum. END NOTES: In a masterpiece
'Alice in Wonderland' which was written by a Mathematician and Logician,
there are many instances of mathematical reasoning between Alice and
Humpty-Dumpty, Alice and Mad Hatter. The conversation between Tweedledum
and Tweedledee have the reeks of reducible logic everywhere. The creator
of 'Simplex Method' in Linear programming, Dantiz starts his book by a
conversation between Alice and Hatter at his tea party which you can
read in 'Through the looking glass'. In which Hatter was insisting Alice
to take some more tea. Alice got irritated and argued that how can she
take more tea when she has none. On it, Hatter replied that probably she
doesn't know how to take less tea. This novel is one of the defining
work which points out the limitation of natural language in describing
'truth'. No wonder Jacquas Derrida came up with his school of thought
'Deconstruction.' See
[here](http://prelectur.stanford.edu/lecturers/derrida/deconstruction.html)
