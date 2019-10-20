from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from .forms import *


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not login'
    context = {'username': username}
    return render(request, 'examples/index.html', context)


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user_profile = profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'examples/register.html', context)


def department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            department.DEPARTMENT = form.cleaned_data.get('DEPARTMENT')
            department.DOCTOR = form.cleaned_data.get('DOCTOR')
            department.save()
            return redirect('department')

    else:
        form = DepartmentForm()
    context = {'form':form}
    return render(request,'examples/department.html',context)


def consult(request):
    if request.method == 'POST':
        consult_form = ConsultForm(request.POST)
        if consult_form.is_valid() :
            consult = consult_form.save(False)

            consult.date1 = consult_form.cleaned_data.get('date1')
            consult.number = consult_form.cleaned_data.get('number')
            consult.date2 = consult_form.cleaned_data.get('date2')
            consult.date3 = consult_form.cleaned_data.get('date3')
            consult.save()
            return redirect('consult')

    else:
         consult_form = ConsultForm()
    context = {'consult_form':consult_form}
    return render(request,'examples/consult.html',context)


#用藥方式
def medicationstyle(request):
    if request.method == 'POST':
        form = MedicationStyleForm(request.POST)
        if form.is_valid():
            medicationstyle = form.save()
            medicationstyle.style = form.cleaned_data.get('style')
            medicationstyle.pcs = form.cleaned_data.get('pcs')
            medicationstyle.save()
            return redirect('medicationstyle')

    else:
        form = MedicationStyleForm()
    context = {'form': form}
    return render(request, 'examples/medicationstyle.html', context)

#用藥須知
def medicationnotice(request):
    if request.method =='POST':
        form = MedicationNoticeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():

            medicationnotice = form.save(False)
            medicationnotice.Durg = form.cleaned_data.get('Durg')
            medicationnotice.save()
            return redirect('medicationnotice')

    else:
        form = MedicationNoticeForm()
        context = {'form': form}
        return render(request, 'examples/medicationnotice.html', context)


#restful api

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset =  Department.objects.all()
    serializer_class = DepartmentSerializer


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


class MedicationStyleViewSet(viewsets.ModelViewSet):
    queryset =  MedicationStyle.objects.all()
    serializer_class =  MedicationStyleSerializer


class MedicationNoticeViewSet(viewsets.ModelViewSet):
    queryset =  MedicationNotice.objects.all()
    serializer_class =  MedicationNoticeSerializer


class MedicationRecordViewSet(viewsets.ModelViewSet):
    queryset =  MedicationRecord.objects.all()
    serializer_class =  MedicationRecordSerializer