from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import FloorType , Room , ExtraServices
from django.shortcuts import redirect
from stuff.models import Stuff

def index(request):
  if request.method == 'POST':
    if request.POST['formFor'] == 'addRoom':
      roomNumberVal = request.POST['roomNumber']
      floorTypeVal = request.POST['floorType']
      priceVal = request.POST['price']

      room = Room(roomNumber=roomNumberVal, floorType=floorTypeVal ,price=priceVal)
      room.save()
      return HttpResponseRedirect("/stuff/room")
    
    if request.POST['formFor'] == 'editRoomFormData':
      roomId = request.POST['roomId']
      newRoomNumber = request.POST['newRoomNumber']
      room = Room.objects.get(id=roomId)
      newRoomNumber = request.POST['newRoomNumber']
      room.roomNumber = newRoomNumber
      room.save()
      return HttpResponseRedirect("/stuff/room")
    
    if request.POST['formFor'] == 'deleteRoomFormData':
      roomId = request.POST['roomId']
      room = Room.objects.get(id=roomId)
      room.delete()
      return HttpResponseRedirect("/stuff/room")
    
    if request.POST['formFor'] == 'addFloor':
      priceVal = request.POST['price']
      floorTypeVal = request.POST['floorType']

      floor = FloorType(floorType=floorTypeVal ,price=priceVal)
      floor.save()
      return HttpResponseRedirect("/stuff/room")
    
    if request.POST['formFor'] == 'addExtra':
      serviceType = request.POST['extraServiceTypeValue']
      priceVal = request.POST['extraPrice']

      extra = ExtraServices(serviceType=serviceType ,price=priceVal)
      extra.save()
      return HttpResponseRedirect("/stuff/room")
    
    if request.POST['formFor'] == 'editExtraForm':
      price = request.POST['price']
      extraId = request.POST['extraId']
      extra = ExtraServices.objects.get(id=extraId)
      extra.price = price
      extra.save()
      return HttpResponseRedirect("/stuff/room")    
    if request.POST['formFor'] == 'editFloorForm':
      price = request.POST['price']
      floorId = request.POST['floorId']
      # floorType = request.POST['floorType']
      floor = FloorType.objects.get(id=floorId)
      # floor.floorType = floorType
      floor.price = price
      floor.save()
      return HttpResponseRedirect("/stuff/room")    
        
    if request.POST['formFor'] == "deleteExtraFormData":
      serviceTypeId = request.POST['serviceTypeId']

      extra = ExtraServices.objects.get(id=serviceTypeId)
      extra.delete()

      return HttpResponseRedirect("/stuff/room")
    if request.POST['formFor'] == "deleteFloorFormData":
      floorTypeId = request.POST['floorTypeId']
      floorType = request.POST['floorType']
      # delete the floor
      floor = FloorType.objects.get(id=floorTypeId)
      floor.delete()
      # delete all rooms that are in this floor
      rooms = Room.objects.all().values()
      rs=[]
      for room in rooms:
        if (room['floorType'] == floorType):
           rs.append(room['id'])
      for r in rs:
        rm = Room.objects.get(id=r)
        rm.delete()

      return HttpResponseRedirect("/stuff/room")
  else:
    if request.user.is_authenticated:
      staffTitle=Stuff.objects.get(stufId=request.user).title
      staffName=Stuff.objects.get(stufId=request.user)
      if staffTitle.lower() == 'cleaner':
        return redirect('Cleaner')
      if request.user.is_staff:
        template = loader.get_template('room.html')
        
        floorType = FloorType.objects.all().values()
        room = Room.objects.all().values()
        extraData = ExtraServices.objects.all().values()
        
        template = loader.get_template('room.html')
        
        context = {
          'floors': floorType,
          'rooms':room,
          'extraServices':extraData,
          'userTitle':staffTitle.lower(),
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        
        return HttpResponse(template.render(context, request))
    return redirect('loginStaff')








