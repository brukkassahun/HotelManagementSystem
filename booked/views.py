from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from reservation.models import Reservation
from room.models import FloorType , Room
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import redirect
from stuff.models import Stuff

class MyView(View):
  def post(self, request):
    staffTitle=Stuff.objects.get(stufId=request.user).title
    staffName=Stuff.objects.get(stufId=request.user)
    if request.POST.get('formFor') == 'bookedEdit':
      inputbookingIdVal = request.POST.get('inputbookingIdVal')
      inputbookingNumberVal = request.POST.get('inputbookingNumberVal')
      inputfirstNameVal = request.POST.get('inputfirstNameVal')
      inputmiddleNameVal = request.POST.get('inputmiddleNameVal')
      inputlastNameVal = request.POST.get('inputlastNameVal')
      inputcontactNumberVal = request.POST.get('inputcontactNumberVal')
      inputemailVal = request.POST.get('inputemailVal')
      inputaddressVal = request.POST.get('inputaddressVal')
      inputidCardTypeVal = request.POST.get('inputidCardTypeVal')
      inputidCardNumberVal = request.POST.get('inputidCardNumberVal')
      inputroomNumberVal = request.POST.get('inputroomNumberVal')
      inputroomNumberOriginalVal = request.POST.get('inputroomNumberOriginalVal')
      inputfloorTypeVal = request.POST.get('inputfloorTypeVal')
      inputcheckInVal = request.POST.get('inputcheckInVal')
      inputcheckOutVal = request.POST.get('inputcheckOutVal')
      inputpaymentStatusVal = request.POST.get('inputpaymentStatusVal')
      inputextraServicesVal = request.POST.get('inputextraServicesVal')
      inputtotalVal = request.POST.get('inputtotalVal')
      
      if inputroomNumberOriginalVal != inputroomNumberVal:
        bookRoom=Room.objects.get(roomNumber=inputroomNumberOriginalVal)
        bookRoom.booking='unbooked'
        bookRoom.save()
        bookRoomSecond=Room.objects.get(roomNumber=inputroomNumberVal)
        bookRoomSecond.booking='booked'
        bookRoomSecond.save()
        
      booking = Reservation.objects.get(id=inputbookingIdVal)
      
      booking.checkIn=inputcheckInVal
      booking.checkOut=inputcheckOutVal
      booking.firstName=inputfirstNameVal
      booking.middelName=inputmiddleNameVal
      booking.lastName=inputlastNameVal
      booking.contactNumber=inputcontactNumberVal
      booking.email=inputemailVal
      booking.address=inputaddressVal
      booking.idCardType=inputidCardTypeVal
      booking.idCardNumber=inputidCardNumberVal
      booking.roomType=inputfloorTypeVal
      booking.roomNumber=inputroomNumberVal
      booking.paymentStatus=inputpaymentStatusVal
      booking.extraServices=inputextraServicesVal
      booking.total=inputtotalVal

      booking.save()
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'bookedPayment':
      id = request.POST.get('BookedId')
      booked = Reservation.objects.get(id=id)
      booked.paymentStatus = 'paid'
      booked.save()
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'checkInFormType':
      idVal = request.POST.get('checkInValInput')
      booked = Reservation.objects.get(id=idVal)
      booked.isCheckedIn = 'true'
      booked.save()
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    if request.POST.get('formFor') == 'checkOutFormType':
      idVal = request.POST.get('checkOutValInput')
      checkOutRoomNumberValInput = request.POST.get('checkOutRoomNumberValInput')
      booked = Reservation.objects.get(id=idVal)
      booked.isCheckedOut = 'true'
      booked.save()
      
      bookRoomSecond=Room.objects.get(roomNumber=checkOutRoomNumberValInput)
      bookRoomSecond.booking='unbooked'
      bookRoomSecond.save()
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'searchForm':
      searchVal = request.POST.get('search')
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.filter(bookingNumber=searchVal)
      numPageList = []
      template = loader.get_template('booked.html')
      if bookingList.count() == 0:
        context = {
          'bookingList': [],
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
      else:
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'filterForm':
      filterVal = request.POST.get('filterForm')
      if (filterVal == 'all'):
        floorType = FloorType.objects.all().values()
        bookingList = Reservation.objects.all().order_by('-id').values()
        paginator = Paginator(bookingList, 8)
        
        page_number = request.GET.get('page')
        bookingList = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1
        
        template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))     
      if (filterVal == 'checkIn'):
        floorType = FloorType.objects.all().values()
        bookingList = Reservation.objects.filter(isCheckedIn='false').all().order_by('-id').values()
        paginator = Paginator(bookingList, 8)
        
        page_number = request.GET.get('page')
        bookingList = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1
        
        template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'checkIn',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
      if (filterVal == 'checkOut'):
        floorType = FloorType.objects.all().values()
        bookingList = Reservation.objects.filter(isCheckedOut='false').all().order_by('-id').values()
        paginator = Paginator(bookingList, 8)
        
        page_number = request.GET.get('page')
        bookingList = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1
        
        template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'checkOut',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.filter(paymentStatus=filterVal).all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
      
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'checkOut',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'filterFormSelect':
      filterVal = request.POST.get('filterFormSelectValue')
      
      floorType = FloorType.objects.all().values()
              
      if (filterVal == 'None'):
        bookingList = Reservation.objects.all().order_by('-id').values()
        template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
      
      if (filterVal == 'All room'):
        bookingList = Reservation.objects.all().order_by('-id').values()
        paginator = Paginator(bookingList, 8)
      
        page_number = request.GET.get('page')
        bookingList = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1   
          template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
      
      bookingList = Reservation.objects.filter(roomType=filterVal).all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1    
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':filterVal,
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponse(template.render(context, request))
    
    if request.POST.get('formFor') == 'deleteBooking':
      id = request.POST.get('deleteIdVal')
      roomNumber = request.POST.get('deleteRoomNumberVal')
      
      bookRoom=Room.objects.get(roomNumber=roomNumber)
      bookRoom.booking='unbooked'
      bookRoom.save()
      
      booked = Reservation.objects.get(id=id)
      booked.delete()
      
      floorType = FloorType.objects.all().values()
      bookingList = Reservation.objects.all().order_by('-id').values()
      paginator = Paginator(bookingList, 8)
      
      page_number = request.GET.get('page')
      bookingList = paginator.get_page(page_number)
      
      numPageList = []
      i=1
      while i <= paginator.num_pages:
        numPageList.append(i)
        i=i+1
     
      template = loader.get_template('booked.html')
      context = {
        'bookingList': bookingList,
        'floors': floorType,
        'numPageList': numPageList,
        'selectStyle':'All room',
        'buttonStyle':'all',
        'userTitle':staffTitle.lower(),
        'staffName':staffName.firstName + ' ' + staffName.lastName
      }
      return HttpResponseRedirect('/stuff/booked')
      
  def get(self, request):
    if request.user.is_authenticated:
      staffTitle=Stuff.objects.get(stufId=request.user).title
      if staffTitle.lower() == 'cleaner':
        return redirect('Cleaner')
      if request.user.is_staff:
        staffName=Stuff.objects.get(stufId=request.user)
        floorType = FloorType.objects.all().values()
        bookingList = Reservation.objects.all().order_by('-id').values()

        paginator = Paginator(bookingList, 8)
        
        page_number = request.GET.get('page')
        bookingList = paginator.get_page(page_number)
        
        numPageList = []
        i=1
        while i <= paginator.num_pages:
          numPageList.append(i)
          i=i+1
        
        template = loader.get_template('booked.html')
        context = {
          'bookingList': bookingList,
          'floors': floorType,
          'numPageList': numPageList,
          'selectStyle':'All room',
          'buttonStyle':'all',
          'userTitle':staffTitle.lower(),
          'staffName':staffName.firstName + ' ' + staffName.lastName
        }
        return HttpResponse(template.render(context, request))
    return redirect('loginStaff')
      








