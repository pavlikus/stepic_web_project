from django.shortcuts import render
from django.http import HttResponse


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')
