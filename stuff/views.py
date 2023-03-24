from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .models import Stuff
from django.shortcuts import redirect
from stuff.models import Stuff

def index(request):
    if request.method == 'POST':
        if request.POST['formType'] == 'addMember':
            stufId=request.POST['userId']
            firstName=request.POST['firstName']
            lastName=request.POST['lastName']
            email=request.POST['email']
            password=request.POST['password']
            title=request.POST['employeeTitle']
            
            u=User.objects.create_user(stufId, email ,password)
            u.first_name=firstName
            u.last_name=lastName
            u.is_staff=True
            u.save() 
            
            newStuff=Stuff(stufId=stufId,firstName=firstName,lastName=lastName,email=email,title=title)
            newStuff.save()
        return redirect('stuff')
        
    else:
        if request.user.is_authenticated:
            staffTitle=Stuff.objects.get(stufId=request.user).title
            staffName=Stuff.objects.get(stufId=request.user)
            if staffTitle.lower() == 'cleaner':
                return redirect('Cleaner')
            if staffTitle.lower() == 'receptionist':
                return redirect('dashboard')
            if request.user.is_staff:
                stuff =Stuff.objects.all().values()
                template = loader.get_template('stuff.html')
                context = {
                    'stuff': stuff,
                    'userTitle':staffTitle.lower(),
                    'staffName':staffName.firstName + ' ' + staffName.lastName
                }
                return HttpResponse(template.render(context, request))
        return redirect('loginStaff')