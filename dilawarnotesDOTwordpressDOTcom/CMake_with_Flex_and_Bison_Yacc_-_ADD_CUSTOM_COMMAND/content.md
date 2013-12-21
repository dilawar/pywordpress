~~~~ 
title: CMake with Flex and Bison (Yacc) : ADD_CUSTOM_COMMAND
type: post
status: publish
id: 702
tag: cmake with flex and bison
category: cmake
~~~~

In case I can not google it again. Here is this informative
[post](http://www.cmake.org/pipermail/cmake/2002-September/003028.html).
Following is the verbatim copy of this email.

    # Create target for the parser
     ADD_CUSTOM_TARGET(FooParser echo "Creating parser.c")

    # Create custom command for flex/lex (note the outputs)
     ADD_CUSTOM_COMMAND(
       SOURCE ${Foo_SOURCE_DIR}/src/lexer.l
       COMMAND ${FLEX_EXECUTABLE} 
       ARGS -o${Foo_BINARY_DIR}/src/lexer.c
            ${Foo_SOURCE_DIR}/src/lexer.l
       TARGET FooParser
       OUTPUTS ${Foo_BINARY_DIR}/src/lexer.c)

    # Create custom command for bison/yacc (note the DEPENDS)
     ADD_CUSTOM_COMMAND(
       SOURCE ${Foo_SOURCE_DIR}/src/parser.y
       COMMAND ${BISON_EXECUTABLE} 
       ARGS -y ${Foo_SOURCE_DIR}/src/parser.y
            -o ${Foo_BINARY_DIR}/src/parser.c
       TARGET FooParser
       DEPENDS ${Foo_BINARY_DIR}/src/lexer.c
       OUTPUTS ${Foo_BINARY_DIR}/src/parser.c)

    # Add parser.c to the list of sources
     SET(Foo_SRCS ${Foo_SRCS} ${Foo_BINARY_DIR}/src/parser.c)

    # Since parser.c does not exists yet when cmake is run, mark
    # it as generated
     SET_SOURCE_FILES_PROPERTIES(${Foo_BINARY_DIR}/src/parser.c GENERATED)

    # Include binary directory to include lexer.c in parser.c
     INCLUDE_DIRECTORIES(${Foo_BINARY_DIR}/src)

                    Andy Cedilnik
                    Kitware Inc.

 
