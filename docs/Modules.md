# Modules

## Imports

Imports in xPython are possible from package or file.
You can import only requested package *(that include only data from `package.xpy`)*
functions, classes, constants or variables.


## Exports

When you need to use some class, function or variable outside of your module - you can make them visible to the external usage. By default all defined classes, functions and variables are visible inside that module only.



### Example

```python
import
  django.db
    models
    models.fields as fields
    migrations
  math
  date
export
  MyClass
  SOME_CONSTANT
  version_name
  some_function


class MyModel extends models.Model
  ...
```

