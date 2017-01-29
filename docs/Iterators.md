# Iterators

Idea is taken from Python language, but a little bit optimized.

When we try to iterate an object - we decorate it with `Iterator` class and every new item we get by call `.next()` method.

## Example

```python
for x in [1, 2, 3]:
  print(x)
# Will be executed internally like this:
it = Iterator([1, 2, 3])
try:
  for x in it.next():
    print(x)
except StopIteration:
  pass
```
## Generarors

Generators used to generate new value on each call of `it.next()`. It's useful when we have big amount of data, that we don't need to place in memory, but want to process value-by-value.

```python
def get_word() -> Dict:
  """Returns next word definition from a textual words-definition dictionary."""
  word_def = {}
  f = open('dictionary.txt')
  for line in f.read_next_line():
    # Empty line splits word definitions.
    if line == "":
      if word_def:
        # Return value as generator.
        return word_def
      continue
    if not word_def:
      word_def['word'] = line.split(' ')[0]
      word_def['examples'] = [line.split(' ')[1]]
    else:
      word_def['examples'].append(line)
  # In the end of the function, if nothing returns it raises StopIteration.

# We always use generators by default for all iterators.
def find_word_definition(word):
  for word_def in get_word():
    if word_def['word'] == word:
      return word_def
  return Null

# It you need to have a list of values - then you need to iterate for all elements and create a list of values.
lst = List(word for word in get_word())
```
