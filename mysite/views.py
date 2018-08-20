from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact_name = form.cleaned_data['contact_name']
            try:
                send_mail(subject, message, from_email, contact_name, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, 'index.html', {'form': form})


def menu(request):
    return render(request, 'menu.html')


def base(request):
    return render(request, 'base.html')


def whine(request):
    return render(request, 'whine.html')


def cocktails(request):
    return render(request, 'cocktails.html')


def lunch(request):
    return render(request, 'lunch.html')

