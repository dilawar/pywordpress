~~~~ 
title: Problem with vector of pointers to struct in C++
type: post
status: draft
id: 539
tag: c++11 standard
tag: vector of struct
category: Programming
~~~~

Following program, although legal in C++11, may not compile with your
current c++ compiler.

~~~~ {.lang-c .prettyprint}
#include    <iostream>
#include    <vector>
using namespace std;

int main()
{
    struct a
    {
        int i;
        int j;
    };

    std::vector<a*> vecA;

    a* pA = new a;

    pA->i = 4;
    pA->j = 9;

    vecA.push_back(pA);

    return 0;
}
~~~~

It may generates following error and refuse to compile.

~~~~ {.lang-c .prettyprint}
struct_update.cc: In function ‘int main()’:
struct_update.cc:32:19: error: template argument for ‘template<class _Alloc> class std::allocator’ uses local type ‘main()::a*’
struct_update.cc:32:19: error:   trying to instantiate ‘template<class _Alloc> class std::allocator’
struct_update.cc:32:19: error: template argument 2 is invalid
struct_update.cc:32:25: error: invalid type in declaration before ‘;’ token
struct_update.cc:39:10: error: request for member ‘push_back’ in ‘vecA’, which is of non-class type ‘int’



The answer is that you should declare your struct outside the main function. A local can not be used as a template parameter (i.e. vectror of pointers to struct).

 For more details, look at this question.
~~~~
