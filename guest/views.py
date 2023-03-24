from django.http import HttpResponse
from django.template import loader
from reservation.models import Reservation
from django.core.paginator import Paginator
from django.shortcuts import redirect
from stuff.models import Stuff
from home.models import UserBookings
from django.contrib.auth.models import User

def index(request):
  if request.method == 'POST':
    staffTitle=Stuff.objects.get(stufId=request.user).title
    staffName=Stuff.objects.get(stufId=request.user)
    if request.POST.get('formFor') == 'filterForm':
      guestId=request.POST['bookingNumberguestId']
      guest = User.objects.filter(is_staff = False)
      history = UserBookings.objects.filter(userId=guestId)
      
      paginator = Paginator(guest, 8)
      
      page_number = request.GET.get('page')
      guest = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      template = loader.get_template('guest.html')
      context = {
        'guest': guest,
        'h': history.order_by('-id'),
        'visibility': True,
        'numPageList': numPageList,
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    if request.POST.get('formFor') == 'searchForm':
      searchVal = request.POST.get('search')
      
      guest = User.objects.filter(username = searchVal)
      # history = UserBookings.objects.get(username = searchVal)
      numPageList = []
      template = loader.get_template('guest.html')
      context = {
        'guest': guest,
        'visibility': False,
        'numPageList': numPageList,
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
  else:
    if request.user.is_authenticated:
      staffTitle=Stuff.objects.get(stufId=request.user).title
      staffName=Stuff.objects.get(stufId=request.user)
      if staffTitle.lower() == 'cleaner':
        return redirect('Cleaner')
      if request.user.is_staff:
        guest = User.objects.filter(is_staff = False)
        history = UserBookings.objects.all().values()

        paginator = Paginator(guest, 8)
        
        page_number = request.GET.get('page')
        guest = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1
        template = loader.get_template('guest.html')
        context = {
          'guest': guest,
          'visibility': False,
          'numPageList': numPageList,
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
    return redirect('loginStaff')