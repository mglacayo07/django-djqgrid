from django.urls import path, include, re_path
from .views import GridView, grid_config, grid_handler, GridView2, GridView4, data, grid
from djqgrid.urls import urlpatterns as djqgrid_patterns

grid_patterns = ([
                     path('', GridView.as_view(), name="basic"),
                     path('2', GridView2.as_view(), name="basic2"),
                     path('3', grid, name="basic3"),
                     path('4', GridView4.as_view(), name="basic4"),
                     path('data', data, name="data"),
                     re_path(r'^examplegrid/$', grid_handler, name='grid_handler'),
                     re_path(r'^examplegrid/cfg/$', grid_config, name='grid_config'),
                     path(r'^grid_json/$', include(djqgrid_patterns)),
                 ], 'grid')
