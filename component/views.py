from django.shortcuts import render
from django.views import generic
from .models import Component

# Create your views here.

class ComponentList(generic.ListView):
    queryset = Component.objects.all()
    template_name = "component/index.html"
    paginate_by = 8