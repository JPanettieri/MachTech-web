from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# Pages

def abouts_us(request):
  return render(request, 'pages/about.html')

def contact_us(request):
  return render(request, 'pages/contact.html')

def landing_freelancer(request):
  return render(request, 'pages/landing-freelancer.html')

def blank_page(request):
  return render(request, 'pages/blank.html')