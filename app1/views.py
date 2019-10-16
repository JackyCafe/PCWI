from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
