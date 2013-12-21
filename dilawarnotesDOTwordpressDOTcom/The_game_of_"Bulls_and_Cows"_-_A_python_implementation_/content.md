~~~~ 
title: The game of "Bulls and Cows" : A python implementation 
type: post
status: publish
id: 963
tag: simple game
tag: ulls and cows
category: Games and Puzzles
category: Python
~~~~

Recently, a friend taught me a simple game of **bulls and cows**. This
game goes like this. There are two players, A and B. A thinks of a
4-letter word and asks B to guess it. Assume that A thought of “link”
and B guesses “lean”. The **bulls** are the number of letters which are
common to both words at the same location in both words , for example
“l” is a bull in "link" and "lean". The **cows**  are number of letters
which are common to both words but not bull. Letter “l” and “n” are
common to both but “l” is the bull, so “n” is the only cow. This guess
or "lean" has one bull and one cow. Player A tells B the number of bulls
and cows. This helps B in making the next guess; the process goes on
till B finds the word. I wrote a python program to play this game on
your computer. I am not sure if it will work on **windows**. It will
definitely work on Linux. Check out repository [implementation of the
game](https://github.com/dilawar/bulls_cows). I will also write an
algorithm which would find the word of A in minimum steps.
