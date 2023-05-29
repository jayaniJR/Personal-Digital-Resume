from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('cv_pdf', views.cv_pdf, name='cv_pdf'),
]