from django.shortcuts import render
from django.http import HttpResponse



def Main(request):
    # selectData=Cake()
    # print(selectData)

    return render(request,"myProjectCakes/index.html")

