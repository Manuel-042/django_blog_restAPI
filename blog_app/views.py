from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def blog_list(request):
    data = {
        "Message": "Hello world"
    }
    
    return JsonResponse(data)
