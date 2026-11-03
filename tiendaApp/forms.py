from django import forms
from django import forms
from .models import Computador, Venta
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from bodegaApp.models import Figura3D # Corregido a Figura3D según tu vista

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['computador', 'figura']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['computador'].queryset = Computador.objects.filter(vendido=False)
        self.fields['figura'].queryset = Figura3D.objects.filter(vendido=False)
        
        self.fields['computador'].widget.attrs.update({'class': 'form-select'})
        self.fields['figura'].widget.attrs.update({'class': 'form-select'})
        
        self.fields['computador'].empty_label = "--- Seleccione un Computador (Opcional) ---"
        self.fields['figura'].empty_label = "--- Seleccione una Figura 3D (Opcional) ---"

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('computador') and not cleaned_data.get('figura'):
            raise forms.ValidationError("Debes seleccionar al menos un Computador o una Figura 3D para registrar la venta.")
        return cleaned_data
    
class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'procesador': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'gpu': forms.TextInput(attrs={'class': 'form-control'}),
            'monitor': forms.TextInput(attrs={'class': 'form-control'}),
            'perifericos': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }

class RegistroUsuarioForm(UserCreationForm):
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.groups.add(self.cleaned_data['grupo'])
        return user

class EditarUsuarioForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.groups.clear()
            user.groups.add(self.cleaned_data['grupo'])
        return user