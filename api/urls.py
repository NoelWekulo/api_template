from django.urls import path, include
from .views import index, RevievViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('review', RevievViewSet)

app_name = 'api'

# Define the URL patterns for the student app
urlpatterns = [
    path('api/', include(router.urls))

    # path('', views.index, name='index'),

   ]