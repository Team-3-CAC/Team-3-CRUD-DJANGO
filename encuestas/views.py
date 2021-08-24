from django.shortcuts import render
from django.http import HttpResponse
from .models import User
import random

# Create your views here.
def home(request):
    return render(request, "base.html")

def saludo(request): # Mauricio
    return HttpResponse("Saludos! desde django para codo a codo")

def welcome(request): # Paola
    return HttpResponse("Bienvenido desde Django para Codo a Codo 4.0")

def datos(request): # Marcos
    return HttpResponse("Por favor complete sus datos personales")

def numero(request): # Fernando
    return HttpResponse(random.randint(0, 5))




def gretting(request):
    myResponse = HttpResponse("Hello world from Django for Codo a Codo 4.0:")

    if request.method == "GET":
        myResponse = read(request)
    elif request.method == "UPDATE":
        myResponse = update(request)
    elif request.method == "QUE VA?":
        myResponse = delete(request)
    else: # Que method es?
        myResponse = create(request)

    return myResponse


    # Que hacemos si un GET?
        # vamos a escribir un IF para determinar si es GET la respuesta devuelve datos.
    # myUsers = User.objects.all() 
    #     output = []
    #     for user in myUsers:
    #    print(user.username)
    #    output.append(user.username)

    # Que hacemos si es un POST?
        # modificar la data
        # myNewUser = User()


def read(request):
    myUsers = User.objects.all()
    print("Hay una cantidad de", len(myUsers), "usuarios registrados actualmente")
    return HttpResponse("READ Hello world from Django for Codo a Codo 4.0:")

def update(data):
    return HttpResponse("UPDATE Hello world from Django for Codo a Codo 4.0:")

def delete(data):
    return HttpResponse("DELETE Hello world from Django for Codo a Codo 4.0:")

def create(data):
    return HttpResponse("CREATE Hello world from Django for Codo a Codo 4.0:")