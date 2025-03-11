from django.test import TestCase
from main.forms import RegistrationForm, ContactForm


class RegistrationFormTest(TestCase):
    def test_valid_registration_form(self):
        """Проверяем, что форма регистрации проходит валидацию"""
        form = RegistrationForm(data={"username": "testuser", "password": "testpass123"})
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        """Проверяем, что пустая форма не проходит валидацию"""
        form = RegistrationForm(data={})
        self.assertFalse(form.is_valid())


class ContactFormTest(TestCase):
    def test_valid_contact_form(self):
        """Проверяем, что форма контактов проходит валидацию"""
        form = ContactForm(data={"name": "Иван", "phone": "+79991234567"})
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        """Проверяем, что форма не валидна без обязательных полей"""
        form = ContactForm(data={"name": ""})
        self.assertFalse(form.is_valid())
