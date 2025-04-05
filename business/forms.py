from django import forms
from django.forms import ModelForm

from business.models import Business


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ('is_suspended', 'is_active')
