from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    return HttpResponse("this is blog home page")

def num(request,num):
    return HttpResponse(f"this is entered num {num}")