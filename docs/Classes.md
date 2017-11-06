# Classes

Class is a user defined [data type](DataTypes.md).
Like any other data type in xPython - class name starts from the capital letter.

Supported multi-inheritance from multiple parent base classes. By default it extends very base class `Type`.

Private, protected and public is here. But all are public by default and this keyword is not needed.

## Example

```python
# Class name always starts from a CapitalLetter.
class _BaseGreeting
  func get_message(): Str
    return 'Hello! It's a local class that can't be accessed outside.'

class UserGreeting extends _BaseGreeting:
  MESSAGES = ['Hello', 'Welcome']
  _name: Str
  _age: Int

  func construct(name: Str, age: Int)
    this.name = name
    this.age = age

  func get_message(msg_id: Int): Str
    greeting = this.MESSAGES[msg_id]
    return "{greeting}, {this.name}! You have {this.age} years."
```
