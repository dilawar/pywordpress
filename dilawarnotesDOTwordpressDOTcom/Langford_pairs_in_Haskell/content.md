~~~~ 
title: Langford pairs in Haskell
type: post
status: publish
id: 505
tag: Haskell
tag: langford pairs
category: Algorithms
category: Haskell
category: Programming
~~~~

  \\This implementation is not-very naive but it is not very efficient
either. It can generate solutions up to n = 12, then it gets very slow.

    This is an extremely horrible solution to generate langford pairs by
    dilawar@ee.iitb.ac.in succesfully finished on Nov 27, 2011 after two days of
    labour. Is is advised not to use this program in any real-time application. Its
    runs slower than Chacha Chaudary brain.

    One can achieve much better performace by using Arrays in Haskell.

    This is discussed in Knuth, TAOP - Vol 4(a)

    > mkZero n = take n [0,0..]

    > genBaseList n
    >     | n < 1 = [] >     | otherwise = n : mkZero n ++ [n]

    We are producing baselists e.g. for n=4, baselists are [1,0,1], [2,0,0,2],
    [3,0,0,0,3] and [4,0,0,0,0,4].

    > allBaseLists n = map genBaseList [n,n-1..1]

    Following horrible step is the core of our algorithm. In this step we use two
    base-list. First list is known as topList while the other one is bottomList. To
    fuse these lists, we first shift the top-list to right by prepending a 0 to it
    and fuse it with bottom. Two lists are no fusable whenver both of them has
    non-zero integer at the same place. This process stops when size of top list
    become more than 2*n we stop. For example, for n = 3

    Top   : 1 0 1    | 0 1 0 1 | 0 0 1 0 1 | 0 0 0 1 0 1 | size more than 2n
    Bot   : 2 0 0 2  | 2 0 0 2 | 2 0 0 2   | 2 0 0 2

    Fuse  : X        | 2 1 0 X | 2 0 1 2 1 | 2 0 0 X
    Nothing    Nothing     Just       Nothing
    ^                        ^
    |                        |
    Two nozero             This is the only
    Entries coincide       possible fusion.

    In second step, we shift the bottom and fuse
    Top   : 1 0 1    | 1 0 1      | 1 0 1         | 1 0 1
    Bot   : 2 0 0 2  | 0 2 0 0 2  | 0 0 2 0 0 2   | size more than 2n

    Fuse  : X        | 1 2 1 0 2  | 1 0 X
    Nothing      Just        Nothing

    > fuseBothList [] y = Just y
    > fuseBothList x [] = Just x
    > fuseBothList (x:xs) (y:ys)
    >     | (x /= 0) && (y /= 0) = Nothing
    >     | otherwise = (helper $ fuseBothList xs ys)
    >                         where helper Nothing = Nothing
    >                               helper (Just p) = if y/=0 then Just (y:p)
    >                                                 else Just (x:p)
    >
    > topRightShiftAndFuse t b n
    >     | length (t) > 2*n = []
    >     | fuseBothList t b == Nothing = topRightShiftAndFuse (0:t) b n
    >     | otherwise = (\(Just p) -> p:(topRightShiftAndFuse (0:t) b n)) (fuseBothList t b)
    >
    >
    > botRightShiftAndFuse t b n
    >     | length (b) > 2*n = []
    >     | fuseBothList t b == Nothing = botRightShiftAndFuse t (0:b) n
    >     | otherwise = (\(Just p) -> p:(botRightShiftAndFuse t (0:b) n)) (fuseBothList t b)
    >
    >

    At each step we get fused lists by above method. These lists are needed to be
    fused with next list And now we should merge what we have fused. For example we
    have got [0,2,0,0,2] and [1,2,1,0,2] from previous merge, now we need to merge
    it with [3,0,0,0,3]. by doing so, we'll get the solution for n=3.

    > mergeTopBottom t b n = (topRightShiftAndFuse t b n) ++ (botRightShiftAndFuse t b n)

    Now rest is putting these function together to get the final solution.

    > initList n = allBaseLists n
    > mergeInto n = (\(x:xs) -> mergeTopBottom (head xs) x n) (initList n)
    > mergeFrom n = (\(x:y:zs) -> zs) (initList n)

    This is my ultimate answer.
    generateSol mergeFromList mergeIntoList n. It generates duplicate solution.

    > generateSol (b:[]) a n
    >     = foldr (++) [] $ map (\x -> mergeTopBottom b x n) a
    > generateSol (b:bs) (a) n
    >     = generateSol bs (foldr (++) [] (map (\x -> mergeTopBottom b x n) a)) n

    And now I should combile all of them to write the top-most function.

    > langfordPair n = generateSol (mergeFrom n) (mergeInto n) n
    > totalPairs n = length (langfordPair n)

    Who needs tests now!
    test1 = mergeTopBottom [2,0,0,2] [3,0,0,0,3] 3
    test2 = map (\x -> mergeTopBottom [1,0,1] x 3) test1
    test4 = mergeThisList [2,0,0,2]
    test5 = mergeThisList
