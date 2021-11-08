from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def support(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        desc = request.POST['desc']
        if len(name)<10 or len(email)<5 or len(phone)<10 or len(address)<10 or len(desc)<5:
            messages.error(request,'Please enter valid details')
        else:
            messages.success(request,'Thank You ! We have recieved your feedback')
            client = Contact(name=name,email=email,phone=phone,address=address,state=state,city=city,pin=pin,desc=desc)
            client.save()
    return render(request,'home/support.html')

def about(request):
    return render(request,'home/about.html')