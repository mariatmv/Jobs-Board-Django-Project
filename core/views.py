from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from job.forms import AddJobForm
from job.models import Job
from userprofile.models import UserProfile


def front_page(req):
    if req.user.is_authenticated:
        jobs = Job.objects.all()
        return render(req, 'index-authenticated.html', {'jobs': jobs})
    return render(req, 'index-not-authenticated.html')


def sign_up(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            userprofile = UserProfile.objects.create(user=user)
            userprofile.save()

            login(req, user)
            return redirect('front page')
    else:
        form = UserCreationForm()

    return render(req, 'signup.html', {'form': form})


def job_details(req, job_id):
    job = Job.objects.get(pk=job_id)
    return render(req, 'job_details.html', {'job': job})


@login_required()
def my_offers(req):
    user_id = req.user.id
    jobs = Job.objects.filter(author_id=user_id)
    return render(req, 'my-offers.html', {'jobs': jobs})


@login_required
def create_offer(req):
    if req.method == 'POST':
        form = AddJobForm(req.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.author = req.user
            job.save()

            return redirect('my offers')
    else:
        form = AddJobForm()

    return render(req, 'create-offer.html', {'form': form})


@login_required
def edit_offer(req, job_id):
    job = get_object_or_404(Job, pk=job_id, author=req.user)
    if req.method == 'POST':
        form = AddJobForm(req.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.author = req.user
            job.save()

            return redirect('job details', job_id)
    else:
        form = AddJobForm(instance=job)

    return render(req, 'edit-offer.html', {'form': form, 'job': job, 'user': req.user})


@login_required
def delete_offer(req, job_id):
    job = get_object_or_404(Job, pk=job_id, author=req.user)

    if req.method == 'POST':
        job.delete()
        return redirect('my offers')

    return render(req, 'delete-offer.html', {'job': job})