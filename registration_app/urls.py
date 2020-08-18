from django.conf.urls import url
from registration_app import views

urlpatterns = [url(r'^$', views.registration, name='register')]