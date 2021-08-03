from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def front_page(req):
    return render(req, 'index.html')


def sign_up(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        user = form.save()

        login(req, user)
        return redirect('front page')
    else:
        form = UserCreationForm()

    return render(req, 'signup.html', {'form': form})