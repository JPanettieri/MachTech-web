from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

        # Pages
    path('', views.index),
    path('about-us/', views.abouts_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('landing-freelancer/', views.landing_freelancer, name='landing_freelancer'),
    path('blank/', views.blank_page, name='blank'),

]
