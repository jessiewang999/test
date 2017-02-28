#coding: utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse("天叔叔，我爱你！")
# Create your views here.
