from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def index(request):

    reviews = Review.objects.all()
    context = {

       'reviews': reviews,
    }

    return render(request, 'index.html')
