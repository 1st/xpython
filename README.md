# xPython

xPython provides a python-like syntax and converters to any language.

It's implementation of an *"ideal language"* that has nice syntax and almost all things that we love in other programming languages.

Idea is to define a syntax with static typing, but with late type binding. Syntax that very similar to **Python**, but at the same time allows to avoid some problems of the language *(like accessing private and protected properties of the class, check data types of variables, define static variables)*. At the end - we can convert the program to any other language *(Swift, Go, Python, JavaScript and Java)*, that allows to write the same codebase and use different backends to run the resulting code.

## Project building blocks

**Compiler** - program that transforms our source code to a code on another programming language. See [wikipedia](https://en.wikipedia.org/wiki/Compiler)

**Parser** - parses our source code to a special structure, that later used by Code Generator.

**Code Generator** - extension that allows to convert program to a selected programming language. Each code generator rely on it's own syntax and implementation, but uses the same parsed code.

## Documentation

Read full documentation about the xPython in the [docs/](docs/) folder.

## Syntax

It's very basic description of the xPython syntax. You can find it very similar to Python language.

```python
import math.operations as math_operations

class Math
  val: Int?
  default_op = '+'

  def init(val: Int)
    this.val = val

  def add(inc: Int): Int
    return math_operations.do_operation('+', this.val, inc)
  
  def calc(inc: Int, op: Char): Int
    return math_operations.do_operation(op, this.val, y)

# All parameters are passed with specifying their names
math = Math(val = 10)
math.add(inc = 20)
print math.val  # prints: 30
math.calc(inc = 2, op = '*')
```

## Installation

```bash
# Install it.
pip install xpython
# Compile file.
xpython compile --language=python script.xpy
# Or compile all files in folder.
xpython compile --language=js project/
```
