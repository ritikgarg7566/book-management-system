from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from importlib_metadata import requires
from bms import models
from django.contrib.auth.models import User
from django.contrib import messages

def addbook(request):
    if request.user.is_authenticated:
           return render(request,"bms/book.html")
    else:
        return render(request,'bms/signin.html')

def front(request):
    if request.user.is_authenticated:
         p=True
         data=models.bookm.objects.all()
         return render(request,'bms/front.html',{"s":data,"p":p})
    else:
        p=False
        return render(request,'bms/front.html',{'p':p})

def edit(request):
    if request.GET['username']==str(request.user):
        s=models.bookm.objects.get(id=request.GET['bookid'])
        res=render(request,'bms/edit.html',{'s':s})
        return res
    else:
        data=models.bookm.objects.all()
        msg="you can not delete and edit this book , you can delete and edit if you are add book"
        return render(request,'bms/front.html',{"s":data,"p":True,"msg6":msg})

def edit_save(request):
    if request.method=='POST':
        title=request.POST.get("title")
        category=request.POST.get("category")
        aname=request.POST.get("aname")
        pname=request.POST.get("pname")
        id=request.POST.get("hidden")
        username=request.POST.get("username")
        bookfile=request.FILES["bookfile"]
        filetype=request.POST["filetype"]
        s=models.bookm()
        s.id=id
        s.username=username
        s.title=title
        s.category=category
        s.aname=aname
        s.pname=pname
        s.bookfile=bookfile
        s.filetype=filetype
        s.save()
        data=models.bookm.objects.all()
        return render(request,'bms/front.html',{"s":data,"p":True})

def delete(request):
    if request.GET['username'] == str(request.user):
        s=models.bookm.objects.get(id=request.GET['bookid'])
        s.delete()
        data=models.bookm.objects.all()
        return render(request,'bms/front.html',{"s":data,"p":True})
    else:
        data=models.bookm.objects.all()
        msg="you can not delete and edit this book , you can delete and edit if you are add book"
        return render(request,'bms/front.html',{"s":data,"p":True,"msg6":msg})


def searching(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get("title")
            data=models.bookm.objects.filter(title=title)
            return render(request,'bms/front.html',{"s":data,"p":True})
    else:
        return render(request,'bms/signin.html')



def book(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get("title")
            category=request.POST.get("category")
            bookfile=request.FILES["bookfile"]
            filetype=request.POST["filetype"]
            aname=request.POST.get("aname")
            pname=request.POST.get("pname")
            s=models.bookm()
            s.username=request.user
            s.title=title
            s.category=category
            s.bookfile=bookfile
            s.filetype=filetype
            s.aname=aname
            s.pname=pname
            s.save()
            data=models.bookm.objects.all()
            return render(request,'bms/front.html',{"s":data,"p":True})
    else:
            return render(request,'bms/signin.html')





def signup(request):
    return render(request,'bms/signup.html')

def signin(request):
    return render(request,'bms/signin.html')

def addsignupdetails(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        if User.objects.filter(username=username):
            msg='username already exist'
            return render(request,'bms/signup.html',{"msg":msg})
        if User.objects.filter(email=email):
            msg='email address already exist'
            return render(request,'bms/signup.html',{"msg":msg})
        if len(username)>10 or len(username)<6:
            msg='username must be under 10 and uper 6 characters'
            return render(request,'bms/signup.html',{"msg":msg})
        if password !=cpassword:
            msg="password didn't match"
            return render(request,'bms/signup.html',{"msg":msg})
        if not username.isalnum():
            msg='username must be alpha-numeric'
            return render(request,'bms/signup.html',{"msg":msg})

        user1=User.objects.create_user(username,email,password)
        user1.first_name=fname
        user1.last_name=lname
        user1.save()

        messages.success(request,"your account has been successfully create")
        return HttpResponseRedirect('signin')

def signinrequest(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username ,password=password)
        if user is not None:
            login(request,user)
            data=models.bookm.objects.all()
            p=True
            return render(request,'bms/front.html',{"s":data,"p":p})
        else:
            messages.success(request,"your username and password is wrong plese fill correct username and password")
            return HttpResponseRedirect('signin')
    return HttpResponse()

def signout(request):
    logout(request)
    p=False
    return render(request,'bms/front.html',{"p":p})
