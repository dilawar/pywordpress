~~~~ 
title: Natural Numbers : Definition
type: post
status: publish
id: 7
category: Definitions
category: Mathematics
~~~~

How to use natural numbers? That is very easy. We've all learned how to
use natural numbers in school. But it is hard to answer; "How to define
natural numbers?". And harder would be; "How to define the actions we do
on natural numbers such as multiplication or addition?" Terrence Tao has
discussed these issues beautifully in his book and I recommend that one
should get this book and read Chapter 2 and 3 [1].

Here we discuss one of the methods to define natural numbers.

[**Defining Natural Numbers : Peano Axioms**](http://en.wikipedia.org/wiki/Peano_axioms)
----------------------------------------------------------------------------------------

These axioms are the standard way to define natural numbers (Can you
build your own set of axioms? This will be a nice exercise. Please let
me know.). Let's first solve our first problem. To use natural numbers
we have to write them down. How to write down the natural numbers? We
use standard figures of 0, 1, 2, 3, etc. to represent them, but we would
not take this for granted. But to start, we need some raw material. This
raw material is the minimum required to build our structure called
natural numbers. For example, if we wish to build the wall, we need
bricks. If we are bold enough, we can start from clay and make the
bricks by ourselves. Well, I'd like to have superpowers so that I can
make silica by myself. All  needed were fundamental particles. One can
again ask whether I can start from more fundamental. This is where we
are restricted by our imagination. Anyway, to build our structure of
natural numbers, we start with two things. Lets assume that someone has
given them to us, one is the number 0 (zero) and one is increment
operator `++` and we collect all the natural number in a set (a
mathematical basket) of Natural numbers represented by \$latex
\\mathbb{N})\$. **Operator `++` :**If we apply this operator to any of
the natural number, we get the **NEXT** natural number. So **0++** is
our next natural number ('1' is saner way to write this number). Next in
line will be (0++)++ (or 2) and ((0++)++)++ (3) and so on. Now we bring
in these axioms known as Peano Axioms.

**Axiom 1.***0 is a natural number.*

No, you can not ask any question, you mortal earthling!

**Axiom 2.***if n is a natural number then n++ is a natural number.*

We start from 0 and apply this axiom once. We get 0++ aka 1 in this big
empty world. Apply this axiom again and we get (0++)++ aka 2. Now if
someone ask you to prove that 5 is a natural number, then invoke axiom 1
and apply axiom 2 five times and do not forget to laugh at his face.
[wink, wink]. These two axioms seems to be enough to build natural
numbers. But world is not filled with ordinary people only : there are
mathematicians too and these mathematicians do not like each other.
Consider two mathematicians, Superman and Lax Luthor. Superman gave
these two axioms and thought that he saved the day. But next day Lax
Luthor came up with his evil argument. He argues (fortunately
anti-Superman Lax Luthor only argues) that as soon as he goes up to some
number say 7, next time Supey invokes axiom 2, He'll wrap back to 0,
i.e. 7++ = 0. What you gonna do about it pretty face? These two axioms
still holds but out natural number set \$latex \\mathbb{N}\$ will
contain numbers from this series 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2
....

**Axiom 3 :***0 is not the successor of any natural number, i.e. there
is no number n such that n++ = 0.*

Lax now argues, "Ok, fine! 7++ is not equal to 0. Let say 7++ is now
equal to 1 or 2 or 3 etc. This will not contradict with any of
Superman's axioms. If 7++ = 2 then my system is 0 1 2 3 4 5 6 7 2 3 4 5
6 7 2 3 4 5 6 ....

**Axiom 4:***Different natural numbers have different successors; i.e.,
if n, m are two different natural numbers than n++ and m++ are also
different natural numbers. EQUIVALENTLY if m++ = n++ then we must have m
= n.*

Now what Lax! All natural numbers are now distinct. 7++ can not be equal
to 2 because there is another number 1 such that 1++ = 2. According to
this axiom, 7++ and 1++ must be different. Should Superman think that he
is done? Wait! Lax Luthor is not considered one of the top ranked super
villain for nothing. He now argues that 0.5, 1.5, 2.5 etc are also
natural numbers. He is introducing '*rogue elements'.*Now it is Superman
primary duty to keep rogue elements away from Mathematics. Sure, one can
argue that one can never get 0.5, 1.5 etc if he starts building natural
numbers from 0 using these axioms. But how Superman will prove this. How
does he know when 0.5 will never apears in \$latex \\mathbb{N}\$.
Superman can keep constructing natural number till the end of time and
Lax will keep saying, 'You have not exhaused all possibilities. Keep it
coming!".

How superman will make this *Lakshman Rekha*to keep these rogue elements
out of \$latex \\mathbb{N}\$. Can Superman get away from it by stating,
"You can never get 0.5 in Natual numbers becasue 0.5 is between 0 and 1
and you can produce any number between 0 and 1." But it will be very
difficult for Mathematical League (not the creepy Justice League. to
quantify what Superman means by "0.5 is between 0 and 1". How can he say
that 0.5 lies between 0 and 1? Is there any proof?

**Axiom 5\* :**(Principle of Mathematical Induction) *Let P(n) be any
property pertaining to natural number n. Suppose that P(0) is true, ans
suppose that when P(n) is true, P(n++) is also true. Then P(n) is true.*

What does Superman mean by 'property' is hard to say at this point. For
example P(n) might be "n is prime"; "n is odd"; "n solve a given
equation".

Now P(n) is such that p(0) is true; and whenever P(n) is true, P(n++) is
also true. The since P(0) is true P(0++) aka P(1) is true. Since P(1) is
true so is P(1++) i.e. P(2) is true and so one. If this fail with
P(0.5), then 0.5 is not an natural number. We can use a simple proof
given in [2] to keep the rogue elements 0.5, 1.5 etc out of \$latex
\\mathbb{N}\$.

***Proof :*******We will be needing integers without defining them. We
borrow the definition of integers. Lets say P(n) = n  "is not a half
integer" i.e. an integer plus 0.5. Then P(0) is true. And if P(n) is
true, then P(n++) is true.  Thus this axiom assert that P(n) is true for
all natural numbers n, i.e. no natural number can be half integer; and
P(0.5) fails to pass this test.[2]

> Since this axiom refers not just to variable but also to PROPERTIES,
> it should technically be called 'axiom schema' rather than an axiom -
> it is a template for producing an infinite number of axioms, rather
> than being a simple axiom in its own right. [Analysis I, Terence Tao.
> pp 20].

NOTES:

-   [1] It is hard to believe that there could be some people who does
    not have some idea of natural numbers. People use different
    name/figures to speak/write natural numbers. It is believed that
    most of the animals have some idea or sense of natural numbers. A
    bird can be seen in stress if one of her eggs is stolen i.e. she
    knows how to count. Language helps us to represent these numbers.
    However, there is a [study publiashed in
    Science](http://www.nature.com/news/2004/040816/full/news040816-10.html)
    which contradict this view. Apparently their counting system
    consists of three quantity, one, few and many. Go ahead, read this
    story published in Nature.
    [http://www.nature.com/news/2004/040816/full/news040816-10.html](http://www.nature.com/news/2004/040816/full/news040816-10.html)

### READINGS:

-   1. [**Analysis
    I**](http://terrytao.wordpress.com/books/analysis-i/), by [*Terrence
    Tao.*](http://terrytao.wordpress.com/)
