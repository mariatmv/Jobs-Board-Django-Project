from django.contrib.auth.views import LogoutView, LoginView
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from core.views import FrontPageView, SignUpView
from job.views import RecentJobsView, JobDetailView, EditOfferView, DeleteOfferView, MyOffersView, CreateOfferView


class TestUrl(SimpleTestCase):
    def test_front_page_url(self):
        url = reverse('front page')
        self.assertEquals(resolve(url).func.view_class, FrontPageView)

    def test_front_page_url(self):
        url = reverse('front page')
        self.assertEquals(resolve(url).func.view_class, FrontPageView)

    def test_recent_jobs_url(self):
        url = reverse('recent jobs')
        self.assertEquals(resolve(url).func.view_class, RecentJobsView)

    def test_sign_up_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, SignUpView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_job_details_url(self):
        url = reverse('job details', args=['1'])
        self.assertEquals(resolve(url).func.view_class, JobDetailView)

    def test_edit_offer_url(self):
        url = reverse('edit offer', args=['1'])
        self.assertEquals(resolve(url).func.view_class, EditOfferView)

    def test_delete_offer_url(self):
        url = reverse('delete offer', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DeleteOfferView)

    def test_my_offers_url(self):
        url = reverse('my offers')
        self.assertEquals(resolve(url).func.view_class, MyOffersView)

    def test_create_offer_url(self):
        url = reverse('create offer')
        self.assertEquals(resolve(url).func.view_class, CreateOfferView)