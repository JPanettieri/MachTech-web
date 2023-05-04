from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def index(request):
  return render(request, 'pages/index.html')


# Pages

def about_us(request):
  return render(request, 'pages/about.html')


def contact_us(request):
  context = {}
  context['show_modal'] = False
  if request.method == 'POST':
    name = request.POST.get('cname')
    email = request.POST.get('cemail')
    message = request.POST.get('cmessage')
    try:
      send_mail(
        subject = f"New contact message from {name}",
        message = f"Message content: {message}\n from: {name}\n email: {email}",
        from_email = 'connect@zenixion.dev',
        recipient_list=['joshua@mach-tech.com.au'], 
        fail_silently=False,)
      context['show_modal'] = True
    except BadHeaderError:
      return HttpResponse('Invalid header found.')

  return render(request, 'pages/contact.html', context)


def what_we_do(request):
  return render(request, 'pages/what_we_do.html')


def blank_page(request):
  return render(request, 'pages/blank.html')



# Components
def accordion(request):
  return render(request, 'components/accordions.html')

def alerts(request):
  return render(request, 'components/alerts.html')

def badges(request):
  return render(request, 'components/badges.html')

def bootstrap_carousels(request):
  return render(request, 'components/bootstrap-carousels.html')

def breadcrumbs(request):
  return render(request, 'components/breadcrumbs.html')

def buttons(request):
  return render(request, 'components/buttons.html')

def cards(request):
  return render(request, 'components/cards.html')

def dropdowns(request):
  return render(request, 'components/dropdowns.html')

def forms(request):
  return render(request, 'components/forms.html')

def modals(request):
  return render(request, 'components/modals.html')

def navs(request):
  return render(request, 'components/navs.html')

def pagination(request):
  return render(request, 'components/pagination.html')

def popovers(request):
  return render(request, 'components/popovers.html')

def progress_bars(request):
  return render(request, 'components/progress-bars.html')

def tables(request):
  return render(request, 'components/tables.html')

def tabs(request):
  return render(request, 'components/tabs.html')

def toasts(request):
  return render(request, 'components/toasts.html')

def tooltips(request):
  return render(request, 'components/tooltips.html')

def typography(request):
  return render(request, 'components/typography.html')