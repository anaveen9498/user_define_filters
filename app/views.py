from django.shortcuts import render
# Create your views here.



def filter(request):
    d={'data':'HeLO pYthOn DevP' }
    return render(request,'filter.html',d)