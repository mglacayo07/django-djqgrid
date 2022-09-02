from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import MyGrid, ExampleGrid, MyModel
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def data(request):
    data = MyModel.objects.all()
    return JsonResponse({'rows': [{'id': 1, 'name': "ss", 'height': 22, 'description': "ss"}]})


class GridView4(TemplateView):
    template_name = "grid/grid4.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)


def grid_handler(request):
    # handles pagination, sorting and searching
    grid = ExampleGrid()
    print(grid.get_json(request))
    return HttpResponse(grid.get_json(request), content_type="application/json")


def grid_config(request):
    # build a config suitable to pass to jqgrid constructor
    grid = ExampleGrid()
    print(grid.get_config())
    return HttpResponse(grid.get_config(), content_type="application/json")


class GridView2(TemplateView):
    template_name = "grid/grid2.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)


# Create your views here.
def grid(request):
    kw = {
        'title': "Aquí estará el grid",
        'grid': MyGrid(),
        'theme': 'core/themes/redmond/jquery-ui.css'
    }
    return render(request, "grid/grid3.html", kw)


class GridView(TemplateView):
    template_name = "grid/grid.html"

    def get(self, request, *args, **kwargs):
        kw = {
            'title': "Aquí estará el grid",
            'grid': MyGrid(),
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)
