from django.shortcuts import render

from django.shortcuts import render, redirect
from app_6.forms import FormHabitat
from app_6.models import Habitat
from .. import forms

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def list_habitat_view(request):
    habitat = Habitat.objects.all()
    data = {'habitat':habitat}
    return render(request,'habitat_listado.html', data)

def insert_habitat_view(request):
    form = forms.FormHabitat()
    if request.method == 'POST':
        form = FormHabitat(request.POST)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render(request, 'habitat_agregar.html', data)

def delete_habitat_view(request, id):
    habitat = Habitat.objects.get(id = id)
    habitat.delete()
    return redirect('view00')

def update_habitat_view(request, id):
    habitat = Habitat.objects.get(id = id)
    form = FormHabitat(instance=habitat)
    if request.method == 'POST':
        form = FormHabitat(request.POST, instance=habitat)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render(request, 'habitat_agregar.html',data)

