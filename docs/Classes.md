# Classes

Class is a user defined [data type](DataTypes.md).
Like any other data type in xPython - class name starts from the capital letter.

Supported multi-inheritance from multiple parent base classes.

## Example

```python
# Class name always starts from a CapitalLetter.
class BaseGreeting:
  def get_message() -> Str:
    return 'Hello!'

class UserGreeting extends BaseGreeting:
  MESSAGES = ('Hello', 'Welcome')
  Str name
  Int age

  def construct(Str name, Int age):
    this.name = name
    this.age = age

  def get_message(Int msg_id) -> Str:
    greeting = this.MESSAGES[msg_id]
    return '{greeting} {this.name}! You have {this.age} years.'
```
