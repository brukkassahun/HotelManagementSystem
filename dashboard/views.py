from django.http import HttpResponse
from django.template import loader
from reservation.models import Reservation
from room.models import FloorType , Room
from django.shortcuts import redirect
from stuff.models import Stuff

def dashboard(request):
  if request.user.is_authenticated:
    staffTitle=Stuff.objects.get(stufId=request.user).title
    if staffTitle.lower() == 'cleaner':
        return redirect('Cleaner')
    if request.user.is_staff:
      staffName=Stuff.objects.get(stufId=request.user)
      floorType = FloorType.objects.all().values()
      room = Room.objects.all().values()
      reservation = Reservation.objects.all().values()
      stuff=Stuff.objects.all().values()
      availableCount =Room.objects.filter(booking='unbooked')
      bookedRoomCount =Room.objects.filter(booking='booked')
      totalEarnings =0
      for x in reservation:
        totalEarnings=totalEarnings+x['subTotal']
      totalCheckIn=Reservation.objects.filter(isCheckedIn='true')
      
      template = loader.get_template('dashboard.html')
      context = {
        'roomCount': room.count(),
        'floorCount': floorType.count(),
        'reservationCount': reservation.count(),
        'staffCount': stuff.count(),
        'availableCount': availableCount.count(),
        'bookedRoomCount': bookedRoomCount.count(),
        'totalEarnings': totalEarnings,
        'totalCheckIn': totalCheckIn.count(),
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
  return redirect('loginStaff')