from django.shortcuts import render
from django.http import response

# Create your views here.
def index(request):
    return HttpResponse("hey there.")

def post(request):
    return HttpResponse("I'm a single post page.")