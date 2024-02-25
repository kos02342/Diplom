from django import forms
from .models import *


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('manufacturer', 'type', 'quantity', 'price', 'status', 'issues')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('manufacturer', 'type', 'quantity', 'price', 'status', 'issues')


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('manufacturer', 'type', 'quantity', 'price', 'status', 'issues')

