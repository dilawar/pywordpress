~~~~ 
title: Hangman in Haskell
type: post
status: publish
id: 983
tag: Hangman
tag: Haskell
category: Games and Puzzles
category: Haskell
~~~~

I wrote a Haskell implementation of a popular game Hangman. Hangman
thinks of a word and tells you its length. You get that many chance to
guess it. The procedure of guessing is following assuming length of the
word is n.

-   You guess a letter, if the word contains that letter, hangman
    reveals the location of this letter. You still have n more guesses.
-   If the word does not contain your letter, your no of guesses is
    reduced by 1.
-   If you guess the word before n == 0, you live else you die.

You have to get two files from [this
folder](https://github.com/dilawar/algorithms/tree/master/games/hangman);
hangman.hs which contains the code and words which contains all possible
words hangman can guess. Compile it using ghc compiler.

>     ghc --make hangman.hs

Run the binary produced. Have fun.
