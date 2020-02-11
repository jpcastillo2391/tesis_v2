from django.shortcuts import render

# Create your views here.

from django.views import generic
#from .models import Album, Song
# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render



def index(request):
    template = loader.get_template("Base_page/index.html")
    return HttpResponse(template.render(request))

def home_page(request):
    # invoke render shortcut to create HttpResponse object with template html file.
    resp = render(request, 'Base_page/index.html')
    # set reponse headers and values.
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    return resp