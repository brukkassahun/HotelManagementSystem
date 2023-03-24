from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from reservation.models import Reservation
from django.urls import reverse

def index(request):
  bookingList = Reservation.objects.all().order_by('-bookingNumber').values()
  template = loader.get_template('booking.html')
  context = {
    'bookingList': bookingList,
  }
  return HttpResponse(template.render(context, request))

