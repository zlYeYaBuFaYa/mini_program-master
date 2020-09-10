# from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from thirdparty.weather import weather

import json
# Create your views here.


def sayHello(request):
    return HttpResponse("ok")


def query_weather(request):
    city = request.GET["city"]
    response = weather(city)
    return JsonResponse(response)