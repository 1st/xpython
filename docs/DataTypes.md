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

### `Int` - integer number

Some simplifications in code allows to write more human-frieldly code.

```python
size = 1KB  # sets 1024. You can use MB, GB, TB as well
amount = 1M + 20K  # results to 1020000. You can use K, M, B as shortcuts to thousand and million
how_long = 24h * 60min * 60sec  # or 60s/60m, just to mak code more easy to understand (minutes, hours, days - which time is used?)

```
