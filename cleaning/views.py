from django.http import HttpResponse
from django.template import loader
from room.models import FloorType , Room
from django.views import View
from django.shortcuts import redirect
from stuff.models import Stuff

class Cleaner(View):
  def post(self, request):
    staffTitle=Stuff.objects.get(stufId=request.user).title
    staffName=Stuff.objects.get(stufId=request.user)
    if request.POST.get('formFor') == 'filterFormSelect':
      filterVal = request.POST.get('filterFormSelectValue')
      if (filterVal == 'All room'):
        room = Room.objects.all().values()
        floorType = FloorType.objects.all().values()
        print(filterVal)
        template = loader.get_template('cleaning.html')
        
        context = {
          'floors':floorType,
            'rooms':room,
            'buttonStyle':'all',
            'selectStyle':'All room',
            'userTitle':staffTitle.lower(),
            'userTitle':staffTitle.lower(),
            'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))

      room = Room.objects.filter(floorType=filterVal)
      floorType = FloorType.objects.all().values()
      print(filterVal)
      template = loader.get_template('cleaning.html')
      
      context = {
        'floors':floorType,
          'rooms':room,
          'buttonStyle':'all',
          'selectStyle':filterVal,
          'userTitle':staffTitle.lower(),
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'filterForm':
      filterVal = request.POST.get('filterFormVal')
      if filterVal == 'all':
        room = Room.objects.all().values()
        floorType = FloorType.objects.all().values()
        
        template = loader.get_template('cleaning.html')
        
        context = {
          'floors':floorType,
            'rooms':room,
            'buttonStyle':'all',
            'selectStyle':'All room',
            'userTitle':staffTitle.lower(),
            'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
      room = Room.objects.filter(clean=filterVal)
      floorType = FloorType.objects.all().values()
      
      template = loader.get_template('cleaning.html')
      
      context = {
        'floors':floorType,
          'rooms':room,
          'buttonStyle':filterVal,
          'selectStyle':'All room',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    if request.POST.get('formFor') == 'conformCleanForm':
      id = request.POST.get('inputRoomIdCeanVal')
      roomC = Room.objects.get(id=id)
      roomC.clean = 'clean'
      roomC.save()
    if request.POST.get('formFor') == 'conformDirtyForm':
      id = request.POST.get('inputRoomIdDirtyVal')
      roomD = Room.objects.get(id=id)
      roomD.clean = 'dirty'
      roomD.save()
    room = Room.objects.all().values()
    floorType = FloorType.objects.all().values()
    
    template = loader.get_template('cleaning.html')
    
    context = {
      'floors':floorType,
        'rooms':room,
        'buttonStyle':'all',
        'selectStyle':'All room',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
    }
    return HttpResponse(template.render(context, request))
  
  def get(self, request):
    if request.user.is_authenticated:
      staffTitle=Stuff.objects.get(stufId=request.user).title
      staffName=Stuff.objects.get(stufId=request.user)
      if request.user.is_staff:
        room = Room.objects.all().values()
        floorType = FloorType.objects.all().values()
        
        template = loader.get_template('cleaning.html')
        
        context = {
          'floors':floorType,
            'rooms':room,
            'buttonStyle':'all',
            'selectStyle':'All room',
            'userTitle':staffTitle.lower(),
            'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
    return redirect('loginStaff')
