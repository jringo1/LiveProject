from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Politician
from .forms import PoliticianForm


#\IntraGov\views.py

def home(request):
    return render(request, "IntraGov/IntraGov_home.html")

def index(request):
    get_Politicians = Politician.objects.all()
    context = {'Politicians': get_Politicians}
    return render(request, 'IntraGov/IntraGov_index.html', context)

def add_politician(request):
    form = PoliticianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('showPolitician')
    else:
        print(form.errors)
        form = PoliticianForm()
    return render(request, 'IntraGov/IntraGov_create.html', {'form':form})

def details_politician(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's in the proper form
    politician = get_object_or_404(Politician, pk=pk)   #Gets single instance of the politician from the database
    context={'politician': politician}                   #Creates dictionary object to pass the jersey object
    return render(request,'IntraGov/IntraGov_details.html', context)