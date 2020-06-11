from django import forms
from . import models


class SearchForm(forms.Form):
    Movie = forms.CharField()
