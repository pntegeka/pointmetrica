from django_flatpickr.widgets import DatePickerInput
from django import forms
from django.forms import ModelForm

from business.models import Business


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = (
            'is_suspended', 'is_active', 'contacts_verified', 'registration_information_verified','last_updated'
        )

class DateFilterForm(forms.Form):
    starting_date = forms.DateField(
        required=False,
        widget=DatePickerInput(
            attrs={
                "class": "form-control bg-transparent border-0 shadow-none",
                "placeholder": "Start date",
            }
        )
    )
    ending_date = forms.DateField(
        required=False,
        widget=DatePickerInput(
            attrs={
                "class": "form-control bg-transparent border-0 shadow-none",
                "placeholder": "End date",
            }
        )
    )

