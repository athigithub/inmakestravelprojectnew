from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    #return HttpResponse("<h1>hellooo")
    #name="athira"
    return render(request,"index.html")
#def addition(request):
   # a=int(request.GET['num1'])
    #b=int(request.GET['num2'])
    #res=a+b
    #return render(request,'result.html',{'result':res})
