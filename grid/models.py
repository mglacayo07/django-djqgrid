from django.db import models
from djqgrid.grid import Grid
from djqgrid.columns import TextColumn, LinkColumn
from .jqgrid import JqGrid
from django.urls import reverse_lazy


class MyModel(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=100)
    url = models.URLField()
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class ExampleGrid(JqGrid):
    model = MyModel  # could also be a queryset
    fields = ['id', 'name', 'desc', 'url']  # optional
    url = reverse_lazy('grid:grid_handler')
    caption = 'My First Grid'  # optional
    colmodel_overrides = {  # optional
        'id': {'editable': False, 'width': 10},
    }
    extra_config = {
        'multiselect': True,
        'multiboxonly': True,
        'toolbar': [True, 'up'],
        'rownumbers': True,
        'shrinkToFit': True,
        'height':'300px'
    }


class MyGrid(Grid):
    model = MyModel

    name = TextColumn(title='Name', model_path='name')
    height = TextColumn(title='Height', model_path='height', align='right')
    desc = LinkColumn(title='Description', model_path='desc', url_builder=lambda m: m.url)
