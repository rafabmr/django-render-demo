from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Usuarios

# Create your views here.
def index(request):
    return HttpResponse('Hola mundo')

def json(request):
    json = {
        'nombre': 'Rafael',
        'apellido': 'Bautista',
        'edad': 27,
        'islogin': True,
        'tiempo': 127.5
    }
    return JsonResponse(json, json_dumps_params={'indent': 4})

def pagina1(request):
    template = loader.get_template('pagina1.html')
    return HttpResponse(template.render())


def pagina2(request, nombre = 'rafa'):
    template = loader.get_template('pagina2.html')
    data = {
        'nombre': nombre
    }
    return HttpResponse(template.render(data, request))

def pagina3(request):
    template = loader.get_template('pagina2.html')
    data = {
        'nombre': request.GET.get('nombre', '')
    }
    return HttpResponse(template.render(data, request))

def paginamodel(request):
    template = loader.get_template('paginamodel.html')
    data = {
        'usuarios': Usuarios.objects.all().values()
    }
    return HttpResponse(template.render(data, request))
