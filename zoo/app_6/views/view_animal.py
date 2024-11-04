from django.shortcuts import render

from django.shortcuts import render, redirect
from app_6.forms import FormAnimal
from app_6.models import Animal
from .view_habitat import home_view
from .. import forms


def list_animal_view(request):
    animal = Animal.objects.all()
    data = {'animal':animal}
    return render(request,'animal_listado.html', data)

def insert_animal_view(request):
    form = forms.FormAnimal()
    if request.method == 'POST':
        form = FormAnimal(request.POST)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render(request, 'animal_agregar.html', data)

def delete_animal_view(request, id):
    animal = Animal.objects.get(id = id)
    animal.delete()
    return redirect('view00')

def update_animal_view(request, id):
    animal = Animal.objects.get(id = id)
    form = FormAnimal(instance=animal)
    if request.method == 'POST':
        form = FormAnimal(request.POST, instance=animal)
        if form.is_valid():
            form.save()
        return home_view(request)
    data = {'form':form}
    return render(request, 'animal_agregar.html',data)