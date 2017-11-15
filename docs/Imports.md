# Imports

Imports in xPython are possible from package or file.
You can import only requested package *(that include only data from `package.xpy`)*
functions, classes, constants or variables.


## Example

```python
import django.db
  models
  models.fields as fields
  migrations
# Import from a global scope.
import math.factorial
# Import from the file/package that located in the same package as this file.
import math.factorial as my_factorial
```

**Note** that you can't do dynamical import of subpackages or files in the imported package:

```python
import django.db

# You can't import dynamically internal packages or files inside package.
# You have access only to content, that you explicitly imported.
class MyModel extends db.models.Model
  ...

# The right way is to import what do you need (two ways are possible).
# Way #1 - import full package or file.
import django.db.models

class MyModel extends models.Model
  ...

# Way #2 - import only requested class.
import django.db.models as django_models

class MyModel extends django_models.Model
  ...
```
