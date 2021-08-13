from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from job.forms import AddJobForm
from job.models import Job


class RecentJobsView(View):

    def get(self, req, *args, **kwargs):
        jobs = Job.objects.all().order_by('-id')[:3][::-1]
        return render(req, 'jobs-listing.html', {'jobs': jobs})


class JobDetailView(View):
    def get(self, req, job_id):
        job = Job.objects.get(pk=job_id)
        return render(req, 'job_details.html', {'job': job})


class MyOffersView(View):
    def get(self, req):
        user_id = req.user.id
        jobs = Job.objects.filter(author_id=user_id)
        return render(req, 'my-offers.html', {'jobs': jobs})


class CreateOfferView(View):
    template_name = 'create-offer.html'

    def get(self, req, *args, **kwargs):
        form = AddJobForm()
        return render(req, self.template_name, {'form': form})

    def post(self, req, *args, **kwargs):
        if req.method == 'POST':
            form = AddJobForm(req.POST)

            if form.is_valid():
                job = form.save(commit=False)
                job.author = req.user
                job.save()

                return HttpResponseRedirect(reverse_lazy('my offers'))
            else:
                context = {
                    'form': form,
                    'message': 'Please enter valid data!'
                }
                return render(req, self.template_name, {'form': form})


class EditOfferView(View):
    def get(self, req, job_id):
        job = get_object_or_404(Job, pk=job_id, author=req.user)
        form = AddJobForm(instance=job)
        return render(req, 'edit-offer.html', {'form': form, 'job': job, 'user': req.user})

    def post(self, req, job_id):
        if req.method == 'POST':
            job = get_object_or_404(Job, pk=job_id, author=req.user)
            form = AddJobForm(req.POST, instance=job)

            if form.is_valid():
                job = form.save(commit=False)
                job.author = req.user
                job.save()

                return HttpResponseRedirect('/job/' + str(job_id) + '/')


class DeleteOfferView(View):
    def get(self, req, job_id):
        job = get_object_or_404(Job, pk=job_id, author=req.user)
        return render(req, 'delete-offer.html', {'job': job})

    def post(self, req, job_id):
        job = get_object_or_404(Job, pk=job_id, author=req.user)
        job.delete()
        return HttpResponseRedirect(reverse_lazy('my offers'))
