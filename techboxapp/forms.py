from .models import ItemAssigment, Item

from django import forms

class ItemAssignmentForm(forms.ModelForm):
    class Meta:
        model = ItemAssigment
        fields = ['name', 'item']
        widgets = {
            'name': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'item': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

# https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#field-types
