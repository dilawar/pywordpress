~~~~ 
title: Python like string split in Haskell
type: post
status: publish
id: 574
tag: python like split in Haskell
tag: string split in Haskell
category: Haskell
category: Language
category: Programming
~~~~

Following function split a string into a list of strings at a given
string. For example `split "dilawar raw war" "aw"` returns
`["dil", "ar r" " war"]`

    split :: String -> String -> [String]
    split str pat = helper str pat [] [] where 
        helper :: String -> String -> String -> String -> [String]
        helper [] ys n m = [n] ++ []
        helper xs [] n m = [n] ++ (split xs pat)
        helper (x:xs) (y:ys) n m
            | x /= y = helper (xs) pat ((n++m)++[x]) m
            | otherwise = helper xs ys n (m++[y])
