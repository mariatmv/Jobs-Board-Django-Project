"""jobs_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views
from core.views import FrontPageView, SignUpView
from job.views import MyOffersView, CreateOfferView, EditOfferView, DeleteOfferView, JobDetailView, RecentJobsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontPageView.as_view(), name='front page'),
    path('recent/', RecentJobsView.as_view(), name='recent jobs'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('job/<int:job_id>/', JobDetailView.as_view(), name='job details'),
    path('my-offers/', login_required(MyOffersView.as_view()), name='my offers'),
    path('create-offer/', login_required(CreateOfferView.as_view()), name='create offer'),
    path('edit-offer/<int:job_id>/', login_required(EditOfferView.as_view()), name='edit offer'),
    path('delete-offer/<int:job_id>/', login_required(DeleteOfferView.as_view()), name='delete offer'),
]
