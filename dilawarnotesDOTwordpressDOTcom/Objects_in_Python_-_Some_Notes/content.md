~~~~ 
title: Objects in Python : Some Notes
type: post
status: publish
id: 435
tag: Objects in Python
category: Programming
category: Python
~~~~

1.  Objects are ‘data abstraction’ in Python. It is imperative to
    understand how objects are related to each other when one use them
    to represent data.
2.  Every object has three ‘attributes’, identity, type and value.
3.  Identity of an object can NOT be changed once object is created.
    Method id() returns identity of a Python object. At this point,
    memory location of the object is identity of the object.
4.  ‘Type’ of an object is also unchangeable.  ‘type’ tells what are the
    operations this object supports e.g. does it has a length? Function
    type() returns the type of object which in itself an object.
5.  Value of an object can be changed. When one can change value of an
    object, it is called mutable otherwise the object is called
    immutable. In pure functional programming languages such as Haskell,
    variables are immutable i.e. you can not change their values once
    created.
    -   The value of an immutable container object that  contains a
        reference to a mutable object can change when later value is
        changed but the container is still considered immutable.
        Immutability is somewhat more subtle than having the property of
        unchangeable values.
    -   Immutability is also dependent on type of the object. For
        instant number, strings and tuple are immutable but dictionary
        and list are not.

6.  Objects are never explicitly destroyed. When they become unusable
    they are
    [garbage-collected.](http://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29)

