# Data Types

We have list of pre-defined data types, that available in each xPython program.

In xPython all data types starts from the capital letter.

If you need to define your own complex data type - visit [classes](Classes.md) page
to find how to create your own data type.


## Basic data types

 - **Type** - base type for all types. Analog of `T` in Java. Contains some logic, that is used by any data type.
 - **Bool** - boolean value *(True or False)*.
 - **Int** - integer variable *(64 bit)*.
 - **Float** - floating point number. *(Note: check, can we use float instead of decimal,
   or we need to provide this data type as well).*
 - **Str** - unicode string.

## Special data types

 - **Null** - used to check if reference is not set.
 - **True** - boolean true.
 - **False** - boolean false.

## Detailed description of each type

### `Str` - unicode string

User can inject any value to a string with `{variable_name}` syntax.

```python
name = 'James'
msg = 'Hello {name}!'
print(msg)  # Hello James!
```
