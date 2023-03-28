from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

        # Pages
    path('', views.index),
    path('about-us/', views.abouts_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('what-we-do/', views.what, name='what-we-do'),
    path('blank/', views.blank_page, name='blank'),

    # Components
    path('accordion/', views.accordion, name='accordion'),
    path('alerts/', views.alerts, name='alerts'),
    path('badges/', views.badges, name='badges'),
    path('bootstrap-carousels/', views.bootstrap_carousels, name='carousels'),
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('forms/', views.forms, name='forms'),
    path('modals/', views.modals, name='modals'),
    path('navs/', views.navs, name='navs'),
    path('pagination/', views.pagination, name='pagination'),
    path('popovers/', views.popovers, name='popovers'),
    path('progress-bars/', views.progress_bars, name='progress_bars'),
    path('tables/', views.tables, name='tables'),
    path('tabs/', views.tabs, name='tabs'),
    path('toasts/', views.toasts, name='toasts'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('typography/', views.typography, name='typography'),
]
