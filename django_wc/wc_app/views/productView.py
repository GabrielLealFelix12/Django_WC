from django.shortcuts import render

from django.http import HttpResponse

def ProductView(request):
    return HttpResponse("ProductView")