from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    return render(request,'blog/bloghome.html')

def num(request,num):
    return HttpResponse(f"this is entered num {num}")