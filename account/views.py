from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.models import User
from .form import NewUserForm
from django.contrib.auth import login as auth_login , authenticate , logout
from django.contrib import messages

def registration(request):
  if request.POST.get('name'):
    userForm=NewUserForm(request.POST)
    if userForm.isItValid():
      # userForm.save()
      userName = userForm.data['name']
      userEmail = userForm.data['email']
      userpassword = userForm.data['password']
      User.objects.create_user(userName, userEmail,userpassword)
      # template = loader.get_template('login.html')
      return redirect('login')
    else:
        userName = userForm.clean_name()
        userEmail = userForm.clean_email()
        userpassword = userForm.clean_password()
        print("username:",userName)
        print("useremial:",userEmail)
        print("userpassword:",userpassword)
        form = NewUserForm()
        template = loader.get_template('userRegistration.html')
        context={'form':form,'userEmail':userEmail,'userName':userName,'userpassword':userpassword}
        return HttpResponse(template.render(context, request))
  else :
    form = NewUserForm()
    context={'form':form}
    template = loader.get_template('userRegistration.html')
    return HttpResponse(template.render(context, request))
  
def loginView(request):
  if request.method =='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      auth_login(request, user)
      return redirect('index')
    else:
      messages.success(request,("Login Error please try again using the correct information!"))
      template = loader.get_template('login.html')
      return HttpResponse(template.render())
  else:
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


