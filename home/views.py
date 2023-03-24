from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import logout
from room.models import FloorType , Room , ExtraServices
from django.http import JsonResponse
from .models import UserBookings
from reservation.models import Reservation
from datetime import date

def index(request):
  if request.method =='POST':
    if request.POST['actionType'] == 'logout':
      logout(request)
      return redirect('index')
    if request.POST['actionType'] == 'book':
      return redirect('book')
    if request.POST['actionType'] == 'register':
      return redirect('registration')
  else:
    template = loader.get_template('home.html')
    context={'r':request}
    return HttpResponse(template.render(context, request))
  
def profile(request):
  if request.method =='POST':
    if request.POST['actionType'] == 'logout':
      logout(request)
      return redirect('index')
  if request.user.is_authenticated:
    bookingData= UserBookings.objects.filter(userId=request.user.id)
    template = loader.get_template('profile.html')
    context = {
      'booking': bookingData,
    }
    return HttpResponse(template.render(context, request))
  else:
    template = loader.get_template('accessDenied.html')
    context={'r':request}
    return HttpResponse(template.render(context, request))
  
def booking(request):
  if request.user.is_authenticated:
    if request.method =='POST':
      if request.POST.get('formType') == 'ajax':
        floorType = request.POST.get('floorType')
        roomsFiltered = Room.objects.filter(floorType=floorType , booking='unbooked').all()
        # rooms = serializers.serialize("json", roomsFiltered)
        responseData = []
        for x in roomsFiltered:
          responseData.append(x.roomNumber)
        response = { "floorType": responseData }
        return JsonResponse(response)
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
        
        bookingUser = UserBookings(
          userId=request.user.id,
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
        bookingUser.save()

        bookingUser=Room.objects.get(roomNumber=roomNumber)
        bookingUser.booking='booked'
        bookingUser.save()
        
        bookingData= UserBookings.objects.filter(userId=request.user.id)
        template = loader.get_template('profile.html')
        context = {
          'booking': bookingData,
        }
        return redirect('profile')
    else:
      floorType = FloorType.objects.all().values()
      extraServices = ExtraServices.objects.all().values()
      room = Room.objects.all().values()
      template = loader.get_template('book.html')
      context = {
        'floors': floorType,
        'rooms':room,
        'extraServices':extraServices,
      }
      return HttpResponse(template.render(context, request))
  else:
    template = loader.get_template('accessDenied.html')
    context={'r':request}
    return HttpResponse(template.render(context, request))

