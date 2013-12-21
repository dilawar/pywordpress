~~~~ 
title: Lambda function is a great way to define a function inside a function in C++
type: post
status: publish
id: 629
category: Uncategorized
~~~~

Finally, I've decided to use some of the features provided by
[C++11](http://en.wikipedia.org/wiki/C%2B%2B11 "C++11") in my code. I
have been programming in
[Haskell](http://haskell.org "Haskell (programming language)") for some
time, therefore, I naturally started with lambda function. Great thing
about lambdas is that I can define a function inside a function. In most
of the cases it is not necessary and C++ does not allow it anyway
([without using
structures](http://stackoverflow.com/questions/4324763/c-can-we-have-functions-inside-functions)
etc.). But sometimes, ability to declare a function inside another
function saves a lot of typing (which you can waste later on writing
blogs) and increases readability. On the flip side, not many C++
programmers are familiar with lambdas; so a decision should be taken
after consulting your team members. If you are an experienced programmer
who have used lambda before then have a look [at
this](http://www.cprogramming.com/c++11/c++11-lambda-closures.html). I
have heard some nice things about boost-phoenix library too. This
library brings functional programming into C++ world. I've used
boost-spirit and I'd recommend to stay away from it for two reasons :
error message does not make any sense (I am not comfortable with
templates) and it takes a lot of time to compile.
