from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
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
