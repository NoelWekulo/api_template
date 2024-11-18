from django.urls import path

from . import views

app_name = 'api'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),

   ]