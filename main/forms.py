from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    """
    Форма для сбора контактных данных пользователя.

    Поля:
    - name: Имя пользователя (строка, макс. 100 символов).
    - phone: Номер телефона (строка, макс. 20 символов).
    """
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)


class RegistrationForm(forms.ModelForm):
    """
    Форма регистрации нового пользователя на основе модели User.

    Добавленные поля:
    - password_confirm: Подтверждение пароля.

    Использует стандартную модель Django User, включая `username` и `password`.
    """
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Подтверждение пароля"
    )

    class Meta:
        """
        Определяет модель и поля, которые будут использоваться в форме.
        """
        model = User
        fields = ['username', 'password']

    def clean(self):
        """
        Проверяет, совпадают ли введенные пароли.

        Если пароли не совпадают, вызывает исключение forms.ValidationError.
        Возвращает очищенные данные формы.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data
