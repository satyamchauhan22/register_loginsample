from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):
  if request.method=='POST': 
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    email=request.POST['email']
    pass1=request.POST['password1']
    pass2=request.POST['password2']
    if pass1==pass2:
        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username,password=pass1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            messages.info(request,'user created')
            return redirect('/')
    else:
        messages.info(request,'password not matching')
        return redirect('/')
  else:
      return render(request,'index.html')

def loggedin(request):
    if request.method=='POST':
      username=request.POST['username']
      pass1=request.POST['password']
      user=auth.authenticate(username=username,password=pass1)
      if user is not None:
          auth.login(request,user)
          return render(request,'loggedin.html')
      else:
          messages.info(request,'wrong entry')
          return redirect('http://127.0.0.1:8000/loggedin/')
    else:
        return render(request,'login.html')