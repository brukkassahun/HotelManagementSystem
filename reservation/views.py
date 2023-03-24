from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from room.models import FloorType , Room ,ExtraServices
from .models import Reservation
from django.http import JsonResponse
from django.views import View
from datetime import date
from django.shortcuts import redirect
from stuff.models import Stuff

class MyView(View):
  def post(self, request):
    if request.POST.get('formType') == 'reservationData':
      bookingNumber = request.POST.get('bookingNumber')
      checkIn = request.POST.get('floating_check_in')
      checkOut = request.POST.get('floating_check_out')
      firstName = request.POST.get('floating_first_name')
      middelName = request.POST.get('floating_middle_name')
      lastName = request.POST.get('floating_last_name')
      contactNumber = request.POST.get('floating_contact_number')
      email = request.POST.get('floating_email')
      address = request.POST.get('floating_address')
      idCardType = request.POST.get('idChoiceSelectedValue')
      idCardNumber = request.POST.get('floating_selected_id_card_number')
      roomType = request.POST.get('roomTypeSelectedValue')
      roomNumber = request.POST.get('roomNumberSelectedValue')
      extraServices = request.POST.get('extraServiceSelected')
      
      # calculate the total price
      floor = FloorType.objects.filter(floorType=roomType).get()
      extraServicesData = ExtraServices.objects.get(id=extraServices)
      floorPrice = int(floor.price)
      total = 0
      extraServicesTotal=0
      chIn=checkIn.split("-")
      chOut=checkOut.split("-")
      d0 = date(int(chIn[0]),int(chIn[1]),int(chIn[2]))
      d1 = date(int(chOut[0]),int(chOut[1]),int(chOut[2]))
      delta = d1 - d0
      days=delta.days
      if(days < 0):
        total=0
        extraServicesTotal=0
        floorPrice=0
      extraServicesTotal=days*extraServicesData.price
      total=days*floorPrice
     
      booking = Reservation(
        bookingNumber=bookingNumber,
        checkIn=checkIn,
        checkOut=checkOut,
        firstName=firstName,
        middelName=middelName,
        lastName=lastName,
        contactNumber=contactNumber,
        email=email,
        address=address,
        idCardType=idCardType,
        idCardNumber=idCardNumber,
        roomType=roomType,
        roomNumber=roomNumber,
        paymentStatus='paid',
        extraServices=extraServicesData.serviceType,
        totalRoomPrice=total,
        totalExtraServicePrice=extraServicesTotal,
        subTotal=total+extraServicesTotal,
        )
      booking.save()
      
      bookRoom=Room.objects.get(roomNumber=roomNumber)
      bookRoom.booking='booked'
      bookRoom.save()
      
      return HttpResponseRedirect("/stuff/booked")
      
    elif request.POST.get('formType') == 'ajax':
      floorType = request.POST.get('floorType')
      roomsFiltered = Room.objects.filter(floorType=floorType , booking='unbooked').all()
      # rooms = serializers.serialize("json", roomsFiltered)
      responseData = []
      for x in roomsFiltered:
        responseData.append(x.roomNumber)
      response = { "floorType": responseData }
      return JsonResponse(response)
  
  def get(self, request):
    if request.user.is_authenticated:
      staffTitle=Stuff.objects.get(stufId=request.user).title
      staffName=Stuff.objects.get(stufId=request.user)
      if staffTitle.lower() == 'cleaner':
        return redirect('Cleaner')
      if request.user.is_staff:
        floorType = FloorType.objects.all().values()
        extraServices = ExtraServices.objects.all().values()
        room = Room.objects.all().values()
        
        template = loader.get_template('reservation.html')
        
        context = {
          'floors': floorType,
          'rooms':room,
          'extraServices':extraServices,
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
    return redirect('loginStaff')
      








