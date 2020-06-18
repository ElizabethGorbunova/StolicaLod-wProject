from django.shortcuts import render
from django.http import HttpResponse

from .models import Cake

def Main(request):

    myData1 = Cake.objects.values('cake_quantity', 'cake_price' , 'cake_description')
    return HttpResponse(myData1)

def BasePage(request):
    return render(request,"myProjectCakes/index.html" )

    # return render(request, myData1, myData2, myData3)
    # myData =Cake.objects.get(pk=cake_quantity)
    # return render(request, myData)
    # return render(request,"myProjectCakes/index.html")
# Create your views here.
