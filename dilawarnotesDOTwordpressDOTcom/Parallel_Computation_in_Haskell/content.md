~~~~ 
title: Parallel Computation in Haskell
type: post
status: publish
id: 440
tag: concurrency in haskell
tag: Haskell
category: Haskell
category: Programming
~~~~

A parallel program is an multi-threaded program designed to work on a
multi-processor of multi-core processor. You will be a moron to write a
multi-threaded program for a single-core processor. Doing this will not
only reduce the performance but also make the
program unnecessarily complicated. In multi-threaded programs, each
thread do some computationally extensive tasks in parallel with other
thread. Ideally, one should design these tasks to be sent to different
cores to be equally time consuming else one thread has to wait till
other finishes. These are complicated issues and problems in program
design. Haskell is a different language. Unlike most of the other
languages, the thread is not created when we demands. Rather a **spark**
is created. This spark is changed into threads when the *Haskell Run
Time* system finds that a unit in CPU is free and can be utilized. *par*
and *pseq* are immensely useful for making your thread behave in a way
you like. This blog is not a tutorial. For tutorial purpose, one has
have a look at this discussion
[thread](http://stackoverflow.com/questions/2763864/multithreaded-haskell).
I personally recommend tutorial by Satnam and Jones. Here is a code with
which you can play around. This code is taken from the tutorial.
[sourcecode language="scala"] import Control.Parallel import System.Time
{--- FUNCTION - Following function take a number and return its
Fibonacci series number. -} fib :: Int -\> Int fib 0 = 0 fib 1 = 1 fib n
= fib (n-1) + fib (n-2) {- - Another function which takes a list and
create a list of corresponding - Fibonacci series number. - NOTE : For
tutorial purpose, [1..28] is a good value. -} fibList :: [Int] -\> [Int]
fibList [] = [] fibList (x:xs) = fib x : fibList (xs) {--- FUNCTION -
Another function is sumEuler function which returns the number of
element in - a list which are co-prime to the a number (in our case, it
is the largest - number in the list. -} mkList :: Int -\> [Int] mkList n
= [1..n-1] -- there is no need to test upto the last element. coprime ::
Int -\> Int -\> Bool coprime x y = gcd x y == 1 euler :: Int -\> Int
euler n= length . filter (coprime n) \$ mkList n sumEuler :: Int -\> Int
sumEuler = sum . (map euler) . mkList {--- FUNCTION -} sumFibEuler ::
Int -\> Int -\> Int sumFibEuler a b = fib a + sumEuler b {--- FUNCTION -
This function is a parallel version of above function, sumFibEuler. -}
parSumFibEuler :: Int -\> Int -\> Int parSumFibEuler a b = par f (pseq e
(e + f)) where -- It says compute (f + e) with f sparked off! f = fib a
e = sumEuler b {--- FUNTION - Performance measurement functions. -}
secDiff :: ClockTime -\> ClockTime -\> Float secDiff (TOD sec1 psec1)
(TOD sec2 psec2) = fromInteger (psec2 - psec1) / 1e12 + fromInteger
(sec2 - sec1) r1 :: Int r1 = parSumFibEuler 38 5300 r2 :: Int r2 = fib
38 r3 :: Int r3 = sumEuler 5300 main :: IO () main = do t0 \<-
getClockTime pseq r1 (return ()) t1 \<- getClockTime putStrLn ("Sum: "
++ show r1) putStrLn ("Time: " ++ show (secDiff t0 t1) ++ " seconds")
{-RESULTS - On my machine with Intel i3 (2 core processors, following
results were - obtained. - - fib 38 took 22.36 sec - sumEuler took 20.67
seconds - parSumFibEuler took approx 41 seconds. - IRRESPECTIVE OF
CHANGE MADE IN main . -} [/sourcecode]
