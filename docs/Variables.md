# Variables

Variables in xPython starts from a lower-case letter only.

When you define a new variable without initial value - you need to provide data type for it.
In case if you assign any value - data type calculated automatically.

### Types of variables.

**(IT'S A DRAFT)**

* **static** has a value that shared between multiple calls of the same code. Even in the next run of the same code the value will be the same as it was set originally at the first try. This value can be changed. See [wikipedia](https://en.wikipedia.org/wiki/Static_variable).
* **constant** variable can't be reassigned and value can't be changed. Constant variables are defined as all-upper-case letters like this `AGE = 30` and always should have the value set. It's impossible to do this `AGE: Int` because value should be set once and forever. See [wikipedia](https://en.wikipedia.org/wiki/Constant_(computer_programming)).
* **immutable** value can't be changed. We can reassing variable to the new value, but we can't change the data in the variable.
* **mutable** value can be modified in-place. Defined like this: `var_name = 25` or `var_name: Int`.

### Visibility

Value can be set as:
* **local variable** and used inside the scope
* **public variable** that can be accessed outside of the scope

In current programming languages we have local scope (of the module, class and function), but doesn't have a local scope for the calculation blocks. As result we keep unneeded variables.

```
func name_to_domain_name(name: Str)
  if name[0] == 'a'
    first_3_letters = name[:3]
    if first_3_letters == 'xxx'
      throw Exception("We can't use this domain name.")
    prefix = "{name}.{first_3_letters}"
  else
    prefix = name
  # first_3_letters will be still defined here, but we don't need it!
  result = "{prefix}.com"
  return result
```

And proposition how to avoid it:
```
func name_to_domain_name(name: Str)
  if name[0] == 'a'
    prefix = "{name}.{first_3_letters}" with
      first_3_letters = name[:3]
      if first_3_letters == 'xxx':
        throw Exception("We can't use this domain name.")
  else
    prefix = name
  # first_3_letters will NOT be defined here.
  result = "{prefix}.com"
  return result
```

## Examples

```
# You need to specify data type for a variable without initial value.
a: Int
# In this case we assign string, that has type Str. New variable "b" has type Str.
b = "Let's do this World amazing!"
# We can define variable like this, and it has type Int, but without initial value.
c = Int("10")
# When we call function - the variable type will be the same, as return value of the function.
d = add(3, 4)
# But be carefull! If you will try to assign new value with a different data type to
# the variable, that already defined - you will have an error. Because we can't redefine
# data type of a variable that we already defined.
c = "New value. This will show you error, because we tried to set Str to Int variable"
```
