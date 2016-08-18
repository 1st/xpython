# xPython

xPython provides a python-like syntax and converters to any language.

Idea is to define a syntax with static typing, but with late type binding. Syntax that very similar to **Python**, but at the same time allows to avoid some problems of the language *(like accessing private and protected properties of the class, check data types of variables, define static variables)*. At the end - we can convert the program to any other language *(Swift, Go, Python, JavaScript and Java)*, that allows to write the same codebase and use different backends to run the resulting code.

## Project building blocks

**Compiler** - program that transforms our source code to a code on another programming language. See [wikipedia](https://en.wikipedia.org/wiki/Compiler)

**Parser** - parses our source code to a special structure, that later used by Code Generator.

**Code Generator** - extension that allows to convert program to a selected programming language. Each code generator rely on it's own syntax and implementation, but uses the same parsed code.
