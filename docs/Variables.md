# Variables

Variables in xPython starts from a lower-case letter only.

When you define a new variable without initial value - you need to provide data type for it.
In case if you assign any value - data type calculated automatically.

## Examples

```python
# You need to specify data type for a variable without initial value.
Int a
# In this case we assign string, that has type Str. New variable "b" has type Str.
b = "Let's do this World amazing!"
# We can define variable like this, and it has type Int, but without initial value.
c = Int()
# When we call function - the variable type will be the same, as return value of the function.
d = add(1, 5)
# But be carefull! If you will try to assign new value with a different data type to
# the variable, that already defined - you will have an error. Because we can't redefine
# data type of a variable that we already defined.
c = "New value. This will show you error, because we tried to set Str to Int variable"
```
