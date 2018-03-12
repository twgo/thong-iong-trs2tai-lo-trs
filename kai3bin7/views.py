from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def thuan5iap8(request):
    return HttpResponse('''
    <form method='get' enctype="multipart/form-data" action="/thong2tai5">
    <input name="myFile" type="file">
    <input name="submit" type="submit">
    </form>
    ''')


def thong2tai5(request):
    return HttpResponse('''
    XD
    ''')
