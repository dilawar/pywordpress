~~~~ 
title: Check Primality of a number in Haskell
type: post
status: publish
id: 474
tag: Haskell
tag: number theory
tag: primality testing
tag: test prime number
category: Haskell
category: Language
category: Programming
~~~~

**Statement** Define a function isPrime which accepts a number n, and
returns True if n is prime and False otherwise. The easiest way to test
the primality of a number is to test whether it has any factor. This is
usally done by dividing the given number by the smallest prime number
i.e. 2 first. If this divides the number, we declare that the given
number is not prime, else we repeat the process with next prime number.
However this approach requires that we must have a table of prime
numbers. It is not possible to use this approach if such table is not
available. To overcome this difficuly, one can choose to simply divide
the given number by integers starting with 2 till one finds a factor. It
has been proven that for a number N, one need not test beyond the
integer ⌊√N⌋ (Why?). Let us produce a list1 of numbers from 2 to ⌊√N⌋.
Function mkList takes an integer and returns a list of integers. Note
that, in function mkList, we are passing n (with type Integer) to a
function sqrt which only works on Reals. Since, sqrt is only defined for
reals, it is customary to convert its argument to a real before passing
it to function sqrt. We have used fromInteger for this purpose. After
creating a such a list, we need to test whether any element of this list
divides the given number N. Function isAnyFactor is written to determine
this. One can see that it uses another function isFactor which tests if
two numbers are coprime 2 or not. If they are coprime then it return
False, else it returns True. In function isFactor, we built a list of
Boolean values using isFactor recursively. Now, it follows that if all
elements of this list are False, then there is no number between 1 and
√-- N which divides the number N, or, the number is prime. One surely
can do some tricks. Such as by looking at the last digit, we can discard
all even numbers and multiple of 5 etc. [sourcecode language="text"]
\<pre\> {- We need to make a list of integers from 2 to square root of N
-} mkList :: Integer -\> [Integer] mkList n = [2..k] where k = toInteger
(ceiling \$ sqrt \$ fromIntegral n ) {- Check if a number divides
another number. -} isFactor :: Integer -\> Integer -\> Bool isFactor m n
| mod m n == 0 = True | otherwise = False {- This function returns array
of Bool indicating if the element from the list created by mkList is a
factor of the given number or not. -} isAnyFactor :: Integer -\>
[Integer] -\> [Bool] isAnyFactor \_ [] = [False] isAnyFactor z (x:xs) =
isFactor z x : isAnyFactor z xs {- Now test for primality. If a given
number is prime, then all of the elements in the list returned ny
isAnyFactor must be False -} isPrime :: Integer -\> Bool isPrime n = not
\$ or \$ isAnyFactor n (mkList n) [/sourcecode]
![](http://img.zemanta.com/pixy.gif?x-id=816787f3-2f1c-8e3a-b454-918e814eb539)
