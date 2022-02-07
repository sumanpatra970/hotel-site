from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from django.shortcuts import render

from travel_app.models import bookings

def index(request):
    return render(request, 'travel_app/basic.html')

def login(request):
    return render(request, 'travel_app/login.html')

def signup(request):
    return render(request, 'travel_app/signup.html')

def signup_next(request):
    first_name=  request.POST['firstname']
    last_name=  request.POST['lastname']
    email=  request.POST['email']
    password=  request.POST['password']
    re_password=  request.POST['repassword']
    username=first_name+last_name
    if password==re_password:
        user_bot = authenticate(username=username, password=password)
        if user_bot is None:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request,'travel_app/next_four.html',{'user':username})
        else:
            return  render(request,'travel_app/next_three.html',{'user':username})
    else:
        return  render(request,'travel_app/password.html')


def login_next(request):
    global counter
    username =request.POST['username']
    password =request.POST['password']
    users= authenticate(username=username, password=password)
    if users is None:
        return render(request,'travel_app/next_two.html',{'user':username})
        counter=0
    else:
        return render(request,'travel_app/next_one.html',{'user':username})
        counter=1

def booking(request):
    username = request.POST['user']
    password=request.POST['password']
    phone_no = request.POST['phoneno']
    value = int(request.POST['roomvalue'])
    date = request.POST['date_issue']
    coupon = request.POST['coupon']
    userr=authenticate(username=username,password=password)
    if userr is None:
        return render(request, 'travel_app/next_five.html', {'user':username})
    else:
        if coupon=='FIRST50':
            finalvalue = (value * 500)-100
        else:
            finalvalue= (value * 500)
        c=bookings(user=username,phoneno=phone_no,price=finalvalue,date=date,room=value)
        c.save()
        info={'username':username,'phoneno':phone_no,'value':value,'price':finalvalue,'date':date}
        return render(request, 'travel_app/booking.html',{'details':info})

def gallery(request):
    return render(request, 'travel_app/gallery.html')

def about(request):
    return render(request, 'travel_app/about.html')

def bookingform(request):
    return render(request, 'travel_app/bookingform.html')

def offer_1(request):
    return render(request, 'travel_app/offerinvalid.html')

def offer_2(request):
    return render(request, 'travel_app/offervalid.html')

def feedback(request):
    return render(request, 'travel_app/feedback.html')

def completeform(request):
    return render(request, 'travel_app/completeform.html')

def account(request):
    return render(request,'travel_app/account_info.html')

def account_final(request):
    username = request.POST['username']
    password = request.POST['password']
    users = authenticate(username=username, password=password)
    if users is None:
        return render(request, 'travel_app/next_six.html')
    else:
        return render(request, 'travel_app/account.html')