from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Crew


# Create your views here.
def demo(request):
    # name="Akhil"
    obj=Place.objects.all()
    obj1=Crew.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})









# def addition(request):
#     x=request.GET("num1")
#     y = request.GET("num2")
#     z=x+y
#     return render(request,"home.html",{"Result":z})
