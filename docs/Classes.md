# Classes

Class is a user defined [data type](DataTypes.md).
Like any other data type in xPython - class name starts from the capital letter.

Supported multi-inheritance from multiple parent base classes.

## Example

```python
# Class name always starts from a CapitalLetter.
class ClassName:
  MESSAGES = ('Hello', 'Welcome')
  limit = 20
  Str name
  Int age

  def construct(Str name, Int age):
    this.name = name
    this.age = age

  def welcome(Int msg_id):
    return '{greeting} {name}! You have {age} years.'.format(
      ...age=this.age,
      ...name=this.name,
      ...greeting=this.MESSAGES[msg_id])
```
