from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def support(request):
    return HttpResponse("this is support page")

def about(request):
    return HttpResponse("this is about page")