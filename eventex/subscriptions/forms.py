# coding: utf-8

# Django
from django import forms
from eventex.subscriptions.models import Subscription
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'CPF deve ter 11 números'))


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].validators.append(CPFValidator)
