__author__ = 'wlw'

from django import forms
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet


class f(forms.Form):
    id = forms.CharField()


class base(BaseFormSet):
    def add_fields(self, form, index):
        super(base, self).add_fields(form, index)
        form.fields['mid'] = forms.CharField()

    def clean(self):
        print "clean"
        print self.cleaned_data


fset = formset_factory(f, formset=base)