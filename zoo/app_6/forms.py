from django import forms
from app_6.models import Habitat, Animal
from django.utils import timezone
from datetime import datetime



class FormHabitat(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nombre(self):
        inputNombre = self.cleaned_data['nombre']
        if len(inputNombre) > 20:
            raise forms.ValidationError("El nombre de habitat es muy largo")
        elif len(inputNombre) < 8:
            raise forms.ValidationError("El nombre de habitat es muy corto")
        return inputNombre

    def clean_fecha_ingreso(self):
     inputFechaI = self.cleaned_data['fecha_ingreso']
     
     date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]
     
     for fmt in date_formats:
         try:
             parsed_date = datetime.strptime(str(inputFechaI), fmt).date()
             if parsed_date > timezone.now().date():
                 raise forms.ValidationError("La fecha debe ser anterior a la actual.")
             return parsed_date
         except (ValueError, TypeError):
             continue
     
     raise forms.ValidationError("Formato de fecha inválido. Use 'dd/mm/yyyy' o 'yyyy-mm-dd'.")

    def clean_duracion_estancia(self):
        inputInstancia = self.cleaned_data['duracion_estancia']
        if inputInstancia <= 0:
            raise forms.ValidationError("Número de estancia inválido")

        return inputInstancia
    
class FormAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nombre(self):
        inputNombre = self.cleaned_data['nombre_animal']
        if len(inputNombre) > 20:
            raise forms.ValidationError("El nombre de habitat es muy largo")
        elif len(inputNombre) < 3:
            raise forms.ValidationError("El nombre de habitat es muy corto")
        return inputNombre

    def clean_fecha_ingreso(self):
     inputFechaI = self.cleaned_data['fecha_nacimiento']
     
     date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]
     
     for fmt in date_formats:
         try:
             parsed_date = datetime.strptime(str(inputFechaI), fmt).date()
             if parsed_date > timezone.now().date():
                 raise forms.ValidationError("La fecha debe ser anterior a la actual.")
             return parsed_date
         except (ValueError, TypeError):
             continue

     raise forms.ValidationError("Formato de fecha inválido. Use 'dd/mm/yyyy' o 'yyyy-mm-dd'.")

    
