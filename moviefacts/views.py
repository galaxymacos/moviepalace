from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


# Create your views here.
def citizen_kane(request):
    content = """{{movie}} was released in {{year}}."""
    template = Template(content)
    context = Context({"movie": "Citizen Kane", "year": 1941})

    result = template.render(context)
    return HttpResponse(result)


def casablanca(request):
    return render(request, "simple.txt", {"movie": "Casablanca", "year": 1942})
