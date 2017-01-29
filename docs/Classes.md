# Classes

Class is a user defined [data type](DataTypes.md).
Like any other data type in xPython - class name starts from the capital letter.

Supported multi-inheritance from multiple parent base classes. By default it extends very base class `Type`.

Private, protected and public is here. But all are public by default and this keyword is not needed.

## Example

```python
# Class name always starts from a CapitalLetter.
class BaseGreeting:
  def get_message() -> Str:
    return 'Hello!'

class UserGreeting extends BaseGreeting:
  MESSAGES = ('Hello', 'Welcome')
  private Str name
  private Int age

  def construct(Str name, Int age):
    this.name = name
    this.age = age

  def get_message(Int msg_id) -> Str:
    greeting = this.MESSAGES[msg_id]
    return '{greeting} {this.name}! You have {this.age} years.'
```
