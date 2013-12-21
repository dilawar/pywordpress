~~~~ 
title: Hangman game in Haskell
type: post
status: publish
id: 487
tag: hangman game
tag: Haskell
category: Haskell
category: Programming
~~~~

Hangman in Haskell
==================

Rule of Hangman
---------------

You play this game with a man called Hangman. The job of hangman is to
kill you. Hangman is fair and have some rules. He is abided by these
rules.

-   Hangman writes down a secret word. Let the word is *W* and its
    length is *n*.
-   He asks you to guess a letter of *W*. Whenever you guess a letter
    which is in *W*, hangman shows you that part of the word. For
    instance, if the word was `cat` and you guessed 'a' then hangman
    shows you `_a_`. At first correct guess, you get to know the size of
    the word and the position of your guess. If the word contains your
    guessed letter more than one time then hangman also shows them. For
    example, if the word was `tweedledee` and you guessed 'e' then
    hangman shows you `__ee__e_ee`.
-   You have minimum of *n* guesses. Every time you guess right, your
    get one more guess to make i.e. for each correct guess, total number
    of guess you can make in future are same.
-   If you can not guess the correct word in given guesses, hangman
    kills you.

Functions we need
-----------------

Obviously, it requires input-output to system. When hangman inputs the
word, you should not see. For this purpose, we have to disable echo at
`stdin`.

    <import>=
    import System.IO

@ Now we have to read the word from terminal. For this purpose we create
a function `getWord`.

    =
    getWord :: IO String
    getWord = do
        c <- getChar
        if c == '\n'
            then return ""
            else do
                l <- getWord
                return (c:l)

@

##### Checking if a letter is in word

To do this, first we check if a given letter is in word by using
function `posChar`. It returns a list of `Bool` specifying if given
letter exists in the word or not. For example, give a word 'gabbar' and
a letter b, `posChar` returns a list of *[False, False, True, True,
False, False]*.

    +=
    posChar :: [Char] -> Char ->  [Bool]
    posChar [] char = []
    posChar (x:xs) char = (x==char) : (posChar xs char)

It would be useful sometimes, just to see if a letter exists in given
word or not. We can simply create another function `ifContain` using
`foldr`. The idea is to use logical `or` operation on the returned list
from `posChar`.

    +=
    ifContain :: [Char] -> Char -> Bool
    ifContain word c = foldr (||) False (posChar word c)

##### Hangman constructs word from guesses

Now if the guessed letter exists in the word then hangman has to show
the word with guessed letter unmasked. We will use letter `_`to mask the
hidden letter. At the beginning, hangman creates a word and a masked
copy of it. Both of them must have the same size. We need a function to
create such a masked copy. To make such a copy, we write a lambda
expression on the fly,

     foldr(\x ->('_':))[] word

does the job nicely. Now the job of hangman is to maintain the mask word
and display its unmasked letter to the player. To maintain it, he needs
a function `addGuessToWord`.

    +=
    addGuessToWord :: [Char] -> [Char] -> Char -> [Char]
    addGuessToWord w w1 c 
        | length(w) /= length(w1) = error "Length mismatch" -- just for safety.
        | ifContain w c = buildW1 w1 c (posChar w c)
        | otherwise = w1
    buildW1 :: [Char] -> Char -> [Bool] -> [Char]
    buildW1 (x:[]) c (p:[])
        | x == '_' && p == True = c:[]
        | x /= '_'  = x:[]
        | otherwise = '_':[]
    buildW1 (x:xs) c (p:ps)
        | x == '_' && p == True = c:buildW1 xs c ps
        | x /= '_'  = x:buildW1 xs c ps
        | otherwise = '_' : buildW1 xs c ps

This function is slightly complicated. It uses extensive pattern
matching. At the heart of this function is another function `buildW1`
which unmasks (or rather put) correct guessed letter into masked-word.

Put things together
-------------------

Now we have all the pieces to play hangman. Now we have to maintain no
of guesses a player is allowed to make and `callHangman` at each step.
We do it by,

    +=
    callHangman :: Int -> [Char] -> [Char] -> Char -> IO ()
    {- No attempt left, you are dead -}
    callHangman 0 wrd wrd1 c = do putStrLn "Dead" 
    {- Attempts left, play on! -}
    callHangman n wrd wrd1 c 
        | ifContain wrd c = do 
            let newWrd = addGuessToWord wrd wrd1 c
            putStrLn (" --> " ++ (show newWrd))
            if wrd == newWrd
                then do
                      putStrLn "Well done!"
                else do
                    putStrLn ("Guess again. Left " ++ (show n))
                    guess <- getChar
                    callHangman n wrd newWrd guess
        | not (ifContain wrd c) = do
            putStrLn ("Guess again. Left " ++ (show (n-1)))
            guess <- getChar
            callHangman (n-1) wrd wrd1 guess
        | otherwise = error "Something wrong in logic."

The main function
-----------------

    =
    main :: IO ()
    main = do
        hSetEcho stdin False -- echo off to get the word from hangman.
        putStrLn "I am going to give you a work to guess."
        word <- getWord
        hSetEcho stdin True -- Now, echo on so player can play.
        let n = (length word)
        putStrLn (show n)
        let emptyWrd = foldr(\x->('_':)) [] word --create a masked copy of word.
        putStrLn emptyWrd
        callHangman (n+1) word emptyWrd ' ' -- dummy call to start the game.
        putStrLn "Game over" -- make sure you are alive ;-)

Program structure
-----------------

    <*>=
    <import>
    <Function>
    <main>

##### Index
