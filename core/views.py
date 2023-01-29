from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome,idade):
    return HttpResponse('Hello {} de {} anos'.format(nome,idade))

def soma(request, valor1,valor2):
    resultado  = valor1 + valor2
    return HttpResponse(' {} + {} = {}'.format(valor1,valor2,resultado))

def subtrair(request, valor1,valor2):
    resultado  = valor1 - valor2
    return HttpResponse(' {} - {} = {}'.format(valor1,valor2,resultado))
def multiplicar(request, valor1,valor2):
    resultado  = valor1 * valor2
    return HttpResponse(' {} X {} = {}'.format(valor1,valor2,resultado))

def dividir(request, valor1,valor2):
    resultado  = valor1 / valor2
    return HttpResponse(' {} / {} = {}'.format(valor1,valor2,resultado))

