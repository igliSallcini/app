from curses.ascii import US
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')

    context = {

        'form':form,
    }
    return render(request,'registration/register.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')
