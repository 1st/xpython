# Imports

Imports in xPython are possible from package or file.
You can import only requested package *(that include only data from `package.xpy`)*
functions, classes, constants or variables.


## Example

```python
from django.db import
  ...models
  ...models.fields as fields
  ...migrations
from math import factorial
```

**Note** that you can't do something like this:

```python
from django import db

# You can't import dynamically internal packages or files inside package.
# You have access only to content, that you explicitly imported.
class MyModel(db.models.Model):  ...

# The right way is to import what do you need (two ways are possible).
# Way #1 - import full package.
from django.db import models

class MyModel(models.Model):  ...

# Way #2 - import only requested class.
from django.db.models import Model

class MyModel(Model):  ...
```
