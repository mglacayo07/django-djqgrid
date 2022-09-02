from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self,request, *args, **kwargs):
        kw = {
            'title': "Django djqGrid example",
            'theme': 'core/themes/redmond/jquery-ui.css'
        }
        return render(request, self.template_name, kw)
