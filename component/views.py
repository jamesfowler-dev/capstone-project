from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Component

# Create your views here.

class ComponentList(generic.ListView):
    queryset = Component.objects.all()
    template_name = "component/index.html"
    paginate_by = 8


def component_detail(request, slug):
    """
    Display an individual :model:`component.Component`.

    **Context**

    ``component``
        An instance of :model:`component.Component`.

    **Template:**

    :template:`component/component_detail.html`
    """

    queryset = Component.objects.filter(status=1)
    component = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "component/component_detail.html",
        {"component": component},
    )