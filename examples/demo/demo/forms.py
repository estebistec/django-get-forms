# -*- coding: utf-8 -*-


from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(required=False)
