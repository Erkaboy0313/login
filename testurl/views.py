from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse('first')
def second(request,id):
    return HttpResponse('second')
def Third(request,id):
    return HttpResponse('third')