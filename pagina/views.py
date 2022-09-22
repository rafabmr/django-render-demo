from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Usuarios

# Create your views here.
def index(request):
    return HttpResponse('Hola mundo')

def json(request, cantidad = 10):

    #cantidad = request.GET.get('cantidad', 0)

    list = []
    for x in range(1, int(cantidad)+1):
        json = {
            'id': x,
            'nombre': 'Nombre '+str(x),
            'apellido': 'Apellido '+str(x),
            'edad': 20+x,
            'islogin': True,
            'tiempo': 127.5
        }
        list.append(json)
    
    return JsonResponse(list, json_dumps_params={'indent': 4}, safe=False)

def pagina1(request):
    template = loader.get_template('pagina1.html')
    return HttpResponse(template.render())


def contador(cantidad):
    list = []
    for x in range(1, int(cantidad)+1):
        json = {
            'id': x,
            'nombre': 'Nombre '+str(x),
            'apellido': 'Apellido '+str(x),
            'edad': 20+x,
            'islogin': True,
            'tiempo': 127.5
        }
        list.append(json)
    return list


def pagina2(request, nombre = ''):
    #template = loader.get_template('pagina2.html')
    data = {
        'nombre': nombre
    }
    return render(request, 'pagina2.html', data)#HttpResponse(template.render(data, request))

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
