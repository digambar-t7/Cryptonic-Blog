from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Contact
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
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
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>10:
        messages.error(request,"Not found")
        bogus = True
        return render(request,'home/search.html',{'bogus':bogus,'query':query})
    posts = BlogPost.objects.filter(title__icontains=query)
    post_head1 = BlogPost.objects.filter(head1__icontains=query)
    post_head2 = BlogPost.objects.filter(head2__icontains=query)
    post_head3 = BlogPost.objects.filter(head3__icontains=query)
    post_desc1 = BlogPost.objects.filter(desc1__icontains=query)
    post_desc2 = BlogPost.objects.filter(desc2__icontains=query)
    post_desc3 = BlogPost.objects.filter(desc3__icontains=query)
    posts = posts.union(post_desc1,post_desc2,post_desc3,post_head1,post_head2,post_head3)
    return render(request,'home/search.html',{'posts':posts})

def signup(request):
    # Get signup user details
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        password = None

        # checks
        if pass1==pass2:
            password = pass1
        else:
            messages.error(request,'Both the entered passwords should match each other')
            return redirect('home')
        
        # Create user using builtin User model
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()

        # redirect back to home page
        messages.success(request,'SUCCESS!Account created')
        return redirect('home')
    
    return HttpResponse('404 Not Found')

def handlelogin(request):
    # getting login details from client
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        # authenticate returns an obj with given username & password
        myuser = authenticate(username=loginusername,password=loginpass)
        print('name is  : '+myuser.first_name)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,f'Welcome {myuser.first_name} ! You have successfully logged in')
        else:
            messages.error(request,'Please enter valid login details & try again')

        return redirect('home')

    return HttpResponse('404 NOT FOUND')

def handlelogout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('home')