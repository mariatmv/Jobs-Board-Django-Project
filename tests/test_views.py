from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
import json

from job.models import Job
from userprofile.models import UserProfile


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('front page')
        self.user = User.objects.create(username='pesho', email='pesho@gmail.com', password='pAr0latanapepi')
        self.job_offer = Job.objects.create(
            title='Job',
            short_description='Jobjobjob',
            long_description='jjjjjjjjjjjjjjjjoooooobbbbbbbb',
            image_url='https://www.roberthalf.com/sites/default/files/2021-04/shutterstock_412257712-2.jpg',
            wage=2000,
            author=self.user,
            # created_on = models.DateTimeField(auto_now_add=True)
            # changed_on = models.DateTimeField(auto_now=True)
            contact_phone='0888774632',
            contact_name='Some Name',
            contact_email='peshp@gmail.com',
            website='http://www.pesho.com',
        )

    # views with only GET requests
    def test_get_unauthorized_front_page(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index-not-authenticated.html')

    def test_get_authorized_front_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs-listing.html')

    def test_get_recent_jobs_view(self):
        response = self.client.get(reverse('recent jobs'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recent_jobs.html')

    def test_get_job_details_view(self):
        response = self.client.get(reverse('job details', args=['1']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'job_details.html')

    def test_get_my_offers_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('my offers'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-offers.html')

    # END of views with only GET requests
