from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from .models import laptops, contact, transaction
from .forms import contactForm, transactionForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    all_laptops =  laptops.objects.all()
    return render(request, 'etrx/index.html',  {'all_laptops': all_laptops })

def detail(request, laptops_id):
    try:
        laptop = laptops.objects.get(pk = laptops_id)
    except laptops.DoesNotExist:
        raise   Http404("Laptop Does Not Exist")
    return render(request, "etrx/detail.html", {'laptop': laptop })


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def success(request, success_id):
    if request.POST:
        form = transactionForm(request.POST)
        if form.is_valid():
            new_c = form.save()
            a = transaction.objects.get(pk=1)
            f = transactionForm(request.POST, instance=a)
            f.save()
            return HttpResponseRedirect('etrx/')
    else:
        form = contactForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'etrx/success.html', args)

def contact_page(request):
    return render(request, 'etrx/contact_page.html')

def contact_thanks(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            new_c = form.save()
            a = contact.objects.get(pk=1)
#           f = contactForm(name="anon", email="anon@ymo.us", query="How do I rate??")
            f = contactForm(request.POST, instance=a)
            f.save()
            return HttpResponseRedirect('etrx/')
    else:
        form = contactForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('etrx/contact_page.html', args)
