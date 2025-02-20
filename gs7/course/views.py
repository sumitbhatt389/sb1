from django.http import HttpResponse
# Create your views here.
def learn_django(request):# pylint: disable=unused-argument
    return HttpResponse("<h1>hello django</h1>")
def learn_python(request):# pylint: disable=unused-argument
    return HttpResponse("<h1>hello python</h1>")