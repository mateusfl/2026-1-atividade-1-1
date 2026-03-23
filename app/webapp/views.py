from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Mateus em SO!")
