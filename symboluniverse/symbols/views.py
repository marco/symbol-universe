from django.shortcuts import render
from django.http import HttpResponse

def symbol(request, id_string):
    id_int = int(id_string)
    symbol = chr(id_int)
    return HttpResponse(symbol)
