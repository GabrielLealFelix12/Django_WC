from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

def HomeView(request):
      home = loader.get_template('templateHome.html')
      return HttpResponse(home.render())