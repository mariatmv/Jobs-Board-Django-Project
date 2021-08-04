from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from job.models import Job


def front_page(req):
    if req.user.is_authenticated:
        jobs = Job.objects.all()
        return render(req, 'index-authenticated.html', {'jobs': jobs})
    return render(req, 'index-not-authenticated.html')


def sign_up(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        user = form.save()

        login(req, user)
        return redirect('front page')
    else:
        form = UserCreationForm()

    return render(req, 'signup.html', {'form': form})


def job_details(req, job_id):
    job = Job.objects.get(pk=job_id)
    return render(req, 'job_details.html', {'job': job})
