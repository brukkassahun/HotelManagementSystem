from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import login as auth_login , authenticate , logout
from django.contrib import messages

  
def loginStaff(request):
  if request.method =='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      auth_login(request, user)
      return redirect('dashboard')
    else:
      messages.success(request,("Login Error please try again using the correct information!"))
      template = loader.get_template('login.html')
      return HttpResponse(template.render())
  else:
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
  
def logoutStaff(request):
  if request.method =='POST':
    if request.POST['actionType'] == 'logout':
      logout(request)
  return redirect('loginStaff')


