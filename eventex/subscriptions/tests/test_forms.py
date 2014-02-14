from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_form_has_fields(self):
        # 'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)
