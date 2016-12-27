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
