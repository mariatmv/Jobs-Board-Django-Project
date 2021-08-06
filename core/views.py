from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from job.models import Job
from userprofile.models import UserProfile


class FrontPageView(View):
    def get(self, req, *args, **kwargs):
        if req.user.is_authenticated:
            jobs = Job.objects.all()
            return render(req, 'jobs-listing.html', {'jobs': jobs})
        return render(req, 'index-not-authenticated.html')



class SignUpView(View):
    template_name = 'signup.html'

    def get(self, req, *args, **kwargs):
        form = UserCreationForm()
        return render(req, self.template_name, {'form': form})

    def post(self, req, *args, **kwargs):
        if req.method == 'POST':
            form = UserCreationForm(req.POST)
            if form.is_valid():
                user = form.save()
                userprofile = UserProfile.objects.create(user=user)
                userprofile.save()

                login(req, user)
                return HttpResponseRedirect(reverse_lazy('front page'))
            else:
                context = {
                    'form': form,
                    'message': 'Please choose a password that matches the requirements!'
                }
                return render(req, self.template_name, context)
