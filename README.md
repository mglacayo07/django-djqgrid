# django jqGrid
Ejemplo de como utilizar el jqGrid en Django

## Técnologias
* Framework: Django [4.1](https://docs.djangoproject.com/en/4.1/)
* Python [3.8.9](https://www.python.org/doc/)
* djqgrid [0.2.4](https://pypi.org/project/djqgrid/)

## Corrección de errores paquete jqGrid
1. Editar el urls.py del paquete instalado
```python
from django.urls import path, include
from .views import query

urlpatterns = [
    path('djqgrid', query),
]
```
2. Editar el archivo views.py. Cambiar la manera de importar `grid_registrar`
```python
import json
from django.http import HttpResponse
from .grid_registrar import get_grid_class

class JsonResponse(HttpResponse):
#...

```
