# -*- coding: utf-8 -*-


from django.db.models import Q
from django.views.generic import ListView
from django_get_forms.views import ProcessGetFormMixin

from .forms import SearchForm
from .models import Article


class SearchView(ProcessGetFormMixin, ListView):
    template_name = 'demo/index.html'
    form_class = SearchForm

    def get_queryset(self):
        if self.form.is_valid() and self.form.cleaned_data['query']:
            query = self.form.cleaned_data['query']
            return Article.objects.filter(
                Q(summary__icontains=query) |
                Q(title__icontains=query) |
                Q(keywords__icontains=query)
            )
        return []


search = SearchView.as_view()
