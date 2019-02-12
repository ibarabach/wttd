from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Ivan Barabach', cpf='12345678900',
                    email='ivan.barabach@gmail.com', phone='47-99971-4042')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):

        expect = 'Confirmacao de inscricao'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@eventex.com.br'

        self.assertEqual(expect,self.email.from_email)

    def test_subscription_email_to(self):

        expect = ['contato@eventex.com.br','ivan.barabach@gmail.com']

        self.assertEqual(expect,self.email.to)


    def test_subscription_email_body(self):

        contents = [
            'Ivan Barabach',
            '12345678900',
            'ivan.barabach@gmail.com',
            '47-99971-4042'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content,self.email.body)

