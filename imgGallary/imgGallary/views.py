from django.shortcuts import render
from imgGallary.models import imggal

def imagedisplay(request):
    resultdisplay = imggal.objects.all()
    return render(request,'index.html',{'imggal':resultdisplay})