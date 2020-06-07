from django.shortcuts import render,redirect
from .models import UserTaskDetails,Profile
from .forms import RegistrationForm,createTicketForm
from django.contrib import messages
import dateutil.parser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .internalOperations import generateCustTaskId
from .operations import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
import json
import os


def home(request):
    return render(request,'custws/home.html')
def userHome(request):
    return render(request,'custws/userhome.html')


@login_required
def profileView(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        dateOfBirth = request.POST.get('dob')
        gender = request.POST.get('gender')
        MobileNo = request.POST.get('mobile')
        website = request.POST.get('website')
        houseNo = request.POST.get('houseNo')
        town=request.POST.get('town')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pin = request.POST.get('pin')

        if first_name:
            request.user.first_name=first_name
            request.user.save()
        if last_name:
            request.user.last_name=last_name
            request.user.save()
        if dateOfBirth:
            request.user.profile.dateOfBirth=dateutil.parser.parse(dateOfBirth)
            request.user.profile.save()
        if gender:
            request.user.profile.gender=gender
            request.user.profile.save()
        if MobileNo:
            request.user.profile.MobileNo=MobileNo
            request.user.profile.save()
        if website:
            request.user.profile.website = website
            request.user.profile.save()
        if houseNo:
            request.user.profile.houseNo=houseNo
            request.user.profile.save()
        if town:
            request.user.profile.town=town
            request.user.profile.save()
        if city:
            request.user.profile.city=city
            request.user.profile.save()
        if district:
            request.user.profile.district = district
            request.user.profile.save()
        if state:
            request.user.profile.state=state
            request.user.profile.save()
        if pin:
            request.user.profile.pin=pin
            request.user.profile.save()


    userdata=User.objects.filter(id=request.user.id)[0]
    profileData=Profile.objects.filter(id=request.user.profile.id)[0]



    context = {'userdata': userdata,'profileData':profileData}
    return render(request,'custws/profile.html',context=context)



def registerPage(request):
    form = RegistrationForm(request.POST)

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Successfully created account')
            return redirect('login')

    context = {'form': form}
    return render(request,'custws/register.html',context=context)

@login_required()
def custDashBoard(request):
    user_id=request.user.id
    query=UserTaskDetails.objects.filter(user_id=user_id).order_by('-custTaskId')
    context={'taskdata':query}

    return render(request,'custws/dashboard.html',context)

@login_required()
def createTicketView(request):
    if request.method == 'POST':
        taskName=request.POST.get('title')
        taskDescription=request.POST.get('description')
        taskCategory=request.POST.get('category')
        taskSubCategory=request.POST.get('type')
        taskRevenue=request.POST.get('price')
        Sla=request.POST.get('sla')
        currency=request.POST.get('currency')
        custTaskId=generateCustTaskId()
        user_id=request.user.id
        task=UserTaskDetails.objects.create(user_id=user_id,taskName=taskName,taskDescription=taskDescription,custTaskId=custTaskId,
                                       taskCategory=taskCategory,taskRevenue=taskRevenue,taskSubCategory=taskSubCategory,
                                       currency=currency,Sla=Sla,taskStatus='CREATED')
        task.save()
        messages.success(request, f'Request Created Succesfully')
        try:
            if sendTaskToTml(createTaskRequestPayload(custTaskId))==200:
                print('Ticket posted to TML')
            else:
                print('Failed posting the request to TML')
        except:
            print('Exception raised by TML')
        return redirect('payment',custTaskId)

    type=['development','testing','support']

    return render(request,'custws/ticket.html',{'title':'create ticket','subcategory':type})


class TicketDetailView(DetailView):
    model = UserTaskDetails

@login_required()
def makePayment(request,id):
    if request.method=='POST':
        try:
            if makePaymentToBRM(createPaymentRequestPayload(id))==200:

                q=UserTaskDetails.objects.filter(custTaskId=id)
                q.update(paymentStatus=True)

                print('Payment Succesful')

            else:
                print('Payment Failure')
        except:
            print('Exception During Payment')
        return redirect('dashboard')

    return render(request,'custws/payment.html')

