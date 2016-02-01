from certificados.models import Usuario, Direccion, Provincia, Ciudad, Transaccion
import models
import json as simplejson
from forms import UsuarioForm, DireccionForm, ProvinciaForm, CiudadForm, TransaccionForm, BuscarUsuarioForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf


def inicio(request):
    aux_usuarios = Usuario.objects.all()
    return render_to_response('certificados/inicio.html', {'usuarios':aux_usuarios}, context_instance=RequestContext(request))


def get_usuario(request):
    if request.method == 'POST':
        formulario = BuscarUsuarioForm(request.POST)
        if formulario.is_valid():
            usuarios_list =[]
            usuario = models.Usuario.objects.get(pk=request.POST['usuario'])
            usuarios_list.adds(usuario)
            return HttpResponseRedirect('/info', {'usuarios':usuarios_list}, context_instance=RequestContext(request))
    else:
        formulario = BuscarUsuarioForm()

    return render_to_response('certificados/informacion_participantes.html', {'formulario':formulario}, context_instance=RequestContext(request))


def usuarios(request):
    usuarios = User.objects.all()
    return render_to_response('certificados/usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))


def crear_usuario(request):
    if request.method=='POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/direccion/nueva')
    else:
        formulario =UsuarioForm()

    return render_to_response('certificados/crear_usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def crear_provincia(request):
    if request.method=='POST':
        formulario = ProvinciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/provincia')
    else:
        formulario = ProvinciaForm()

    return render_to_response('certificados/crear_provincia.html', {'formulario':formulario}, context_instance=RequestContext(request))


def crear_ciudad(request):
    if request.method=='POST':
        formulario = CiudadForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ciudad')
    else:
        formulario = CiudadForm()

    return render_to_response('certificados/crear_ciudad.html', {'formulario':formulario}, context_instance=RequestContext(request))


def crear_direccion(request):
    if request.method=='POST':
        formulario = DireccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/transaccion')
    else:
            formulario = DireccionForm()

    return render_to_response('certificados/crear_direccion.html', {'formulario':formulario}, context_instance=RequestContext(request))


def crear_transaccion(request):
    if request.method == 'POST':
        formulario = TransaccionForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
            formulario = TransaccionForm()

    return render_to_response('certificados/crear_transaccion.html', {'formulario':formulario}, context_instance=RequestContext(request))

def get_ciudades(request, prov_id):
    provincia = models.Provincia.objects.get(pk=prov_id)
    ciudades = models.Ciudad.objects.filter(cod_prov=provincia)
    ciudades_dict = {}
    for ciudad in ciudades:
        ciudades_dict[ciudad.id] = ciudad.nombre

    return HttpResponse(simplejson.dumps(ciudades_dict), mimetype="application/json")