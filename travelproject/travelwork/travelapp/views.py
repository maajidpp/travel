from django.shortcuts import render
from . models import Place
# Create your views here.



def demo(request):
    obj = Place.objects.all()
    context = {"result": obj}

    return render(request,"index.html",context)