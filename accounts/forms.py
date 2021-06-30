from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter password',
            'class':'form-control',
        }
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter Confirm password',
            'class':'form-control',
        }
    ))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone no'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
       cleaned_data = super(RegistrationForm, self).clean()
       password = cleaned_data.get('password')
       confirm_password = cleaned_data.get('confirm_password')
       phone_number = cleaned_data.get('phone_number')
       if password != confirm_password:
           raise forms.ValidationError(
               'Password does not match !'
           )
       if len(phone_number) != 10:
           raise forms.ValidationError(
               'Phone no can not have more than 10 numbers!'
           )
       
        
        
