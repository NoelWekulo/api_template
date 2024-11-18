from django.shortcuts import render, redirect
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Review

# Create your views here.

def index(request):

    reviews = Review.objects.all()
    context = {
       'reviews': reviews,
    }

    return render(request, 'index.html')


class RevievViewSet(ModelViewSet):
   queryset = Review.objects.all()
   serializer_class = ReviewSerializer