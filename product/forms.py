from django import forms

from .models import Product

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ( 'name', 'description', 'price',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ( 'name', 'description', 'price',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

        