from django import forms

from job.models import Job


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'short_description', 'long_description', 'image_url', 'wage',
                  'contact_phone', 'contact_name', 'contact_email', 'website']
