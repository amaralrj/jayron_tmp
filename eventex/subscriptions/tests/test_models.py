# coding : utf-8

# Python
from datetime import datetime

# Django
from django.db import IntegrityError
from django.test import TestCase

# Project
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-96186180'
        )

    def test_create(self):
        # 'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Henrique Bastos', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(
            name='Henrique Bastos', cpf='12345678901',
            email='henrique@bastos.net', phone='21-96186180'
        )

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(
            name='Henrique Bastos', cpf='12345678901',
            email='outro@email.com', phone='21-96186180'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        'Email is not unique anymore'
        s = Subscription.objects.create(name='Henrique Bastos', cpf='109876543210',
                email='henrique@bastos.net')
        self.assertEqual(2, s.pk)
