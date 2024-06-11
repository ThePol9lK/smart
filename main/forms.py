from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)
    
    

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'log-form__input section-descr',
            'placeholder': 'Имя'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'log-form__input section-descr',
            'placeholder': 'Пароль'
        })
    )