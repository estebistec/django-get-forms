# -*- coding: utf-8 -*-


from django.core.exceptions import ImproperlyConfigured
from django.views.generic.base import ContextMixin


class ProcessGetFormMixin(ContextMixin):
    """
    Mixin for views that have forms submitted via HTTP GET.
    """

    form_class = None

    def get_form_class(self):
        """
        Returns the form class to use in this view
        """
        return self.form_class

    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        if not form_class:
            raise ImproperlyConfigured('ProcessGetFormMixin requires that a form_class attribute be defined')
        return form_class(data=self.request.GET)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.form.full_clean()
        return super(ProcessGetFormMixin, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.form
        return super(ProcessGetFormMixin, self).get_context_data(**kwargs)
