from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from .models import  SscResult, InterResult1, InterResult2, DegreeResult1, DegreeResult2, DegreeResult3,BtechResult1, BtechResult2, BtechResult3, BtechResult4
from django.http import HttpResponse

# Create your views here.

def home(request):
     return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pwd1']
        password2 = request.POST['pwd2']
        if password1 == password2:
            user = User.objects.create_user(username=email, password=password1)
            user.first_name = first_name.upper()
            user.last_name = last_name.upper()
            user.save()
            messages.success(request, f"Hello, {first_name} {last_name} Successfully Created Your Account")
            return redirect('signin')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Id is Already Exist..')
        else:
            messages.info(request, 'Passwords Did Not Match')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Wellcome, {user.first_name} {user.last_name}, Successfully Loged into Your Account")
            return redirect('home')
        else:
            messages.info(request, 'Invalid Password Or Email Id')
    return render(request, 'signin.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')

#------------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def ssc(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if SscResult.objects.filter(name=request.user.id).exists():
            ssc = SscResult.objects.get(name=request.user.id)
            if ssc:
                if hall_ticket_no == ssc.hall_ticket:
                    return render(request,'sscresult.html',{"ssc":ssc})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('ssc')
        else:
            messages.info(request, 'No Record Found')
            return redirect('ssc')
    return render(request, 'ssc.html')

def inter_1y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if InterResult1.objects.filter(name=request.user.id).exists():
            inter = InterResult1.objects.get(name=request.user.id)
            if inter:
                if hall_ticket_no == inter.hall_ticket:
                    return render(request,'inter_result1.html',{"inter":inter})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('inter_1y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('inter_1y')
    return render(request, 'inter_1y.html')

def inter_2y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if InterResult2.objects.filter(name=request.user.id).exists():
            inter = InterResult2.objects.get(name=request.user.id)
            if inter:
                if hall_ticket_no == inter.hall_ticket:
                    return render(request,'inter_result2.html',{"inter":inter})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('inter_2y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('inter_2y')
    return render(request, 'inter_2y.html')

def degree_1y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if DegreeResult1.objects.filter(name=request.user.id).exists():
            degree = DegreeResult1.objects.get(name=request.user.id)
            if degree:
                if hall_ticket_no == degree.hall_ticket:
                    return render(request,'degree_result1.html',{"degree":degree})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('degree_1y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('degree_1y')
    return render(request, 'degree_1y.html')
def degree_2y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if DegreeResult2.objects.filter(name=request.user.id).exists():
            degree = DegreeResult2.objects.get(name=request.user.id)
            if degree:
                if hall_ticket_no == degree.hall_ticket:
                    return render(request,'degree_result2.html',{"degree":degree})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('degree_2y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('degree_2y')
    return render(request, 'degree_2y.html')
def degree_3y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if DegreeResult3.objects.filter(name=request.user.id).exists():
            degree = DegreeResult3.objects.get(name=request.user.id)
            if degree:
                if hall_ticket_no == degree.hall_ticket:
                    return render(request,'degree_result3.html',{"degree":degree})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('degree_3y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('degree_3y')
    return render(request, 'degree_3y.html')

def btech_1y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if BtechResult1.objects.filter(name=request.user.id).exists():
            btech = BtechResult1.objects.get(name=request.user.id)
            if btech:
                if hall_ticket_no == btech.hall_ticket:
                    return render(request,'btech_result1.html',{"btech":btech})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('btech_1y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('btech_1y')
    return render(request, 'btech_1y.html')
def btech_2y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if BtechResult2.objects.filter(name=request.user.id).exists():
            btech = BtechResult2.objects.get(name=request.user.id)
            if btech:
                if hall_ticket_no == btech.hall_ticket:
                    return render(request,'btech_result2.html',{"btech":btech})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('btech_2y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('btech_2y')
    return render(request, 'btech_2y.html')
def btech_3y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if BtechResult3.objects.filter(name=request.user.id).exists():
            btech = BtechResult3.objects.get(name=request.user.id)
            if btech:
                if hall_ticket_no == btech.hall_ticket:
                    return render(request,'btech_result3.html',{"btech":btech})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('btech_3y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('btech_3y')
    return render(request, 'btech_3y.html')
def btech_4y(request):
    if request.method == 'POST':
        hall_ticket_no = int(request.POST.get('hltno'))
        if BtechResult4.objects.filter(name=request.user.id).exists():
            btech = BtechResult4.objects.get(name=request.user.id)
            if btech:
                if hall_ticket_no == btech.hall_ticket:
                    return render(request,'btech_result4.html',{"btech":btech})
                else:
                    messages.info(request, 'Invalid Hall Ticket Number')
                    return redirect('btech_4y')
        else:
            messages.info(request, 'No Record Found')
            return redirect('btech_4y')
    return render(request, 'btech_4y.html')
#----------------------------------------------------
