# Functions

Function is a logical block of program, that allows to make program more readable. Function allows
to define small piece of code and then use it in multiple places, avoiding repeated parts of code if few places.

Function name always starts from a lower-case letter, like a [variable](Variables.md).


## Examples

Function definition.

```
func welcome(name: Str, age: Int, greeting='Hello', ending='sir'): Str
  return "{greeting}, {name}. You are {age} years old, correct {ending}?"

func _localFunction()
  print("It's a local function and can't be accessed outside of the current scope (module/class/function).")
```

Usage of a function.

```
welcome('James', 25)
welcome('James', 25, 'Hi')
welcome('James', 25, ending: 'man')

# This format allows to simplify readability of the multiple parameters.
# It's a preferred way to call a function with many parameters.
welcome
  name: 'James'
  age: 25
  greeting: 'Hi'

# We can pass dynamically changed parameter names.
# It allows to highlight the variable alongside other parameter names.
paramName = 'greeting'
welcome
  name: 'James'
  age: 25
  $paramName: 'Hi'
```
