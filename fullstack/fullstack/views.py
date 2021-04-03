from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import  json
import requests
def mainPage(request):
    template_name = 'hello.html'
    return render(request,template_name)
def getData(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)
def getReddit(request):
    response = requests.get("https://www.reddit.com/.json")
    data = response.json()
    return JsonResponse(data)

def checkRequest(request):
    print(request.headers)
    val = request.GET.dict()
    print(val)
    testVal = request.GET.get('something')
    return HttpResponse(testVal)
