# coding: utf-8

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Project
from src.subscriptions.models import Subscription
from src.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})
    obj = form.save()
    return HttpResponseRedirect('/inscricao/%d/' % obj.pk)


def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)

    return render(
        request, 'subscriptions/subscription_detail.html', {'subscription': subscription}
    )
