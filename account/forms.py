from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requried. Add a valid email address.')
    class Meta:
        model = Account
        fields = ('email', 'username', 'phone_number', 'password1', 'password2',)


class AccountAuthenticationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('email', 'password')	
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")    


class AccountUpdateForm(forms.ModelForm):

	class Meta:
	    model = Account
	    fields = ('email','username','phone_number',)
     
	def clean_email(self):
	    email = self.cleaned_data['email']
	    try:
	        account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
	    except Account.DoesNotExist:
	        return email
	        raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_contact(self):
	    phone_number = self.cleaned_data['phone_number']
	    try:
	        account = Account.objects.exclude(pk=self.instance.pk).get(phone_number=phone_number)
	    except Account.DoesNotExist:
	        return phone_number
	        raise forms.ValidationError('Phone Number "%s" is already in use.' % account)

	def clean_username(self):
	    username = self.cleaned_data['username']
	    try:
	        account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
	    except Account.DoesNotExist:
	        return username
	        raise forms.ValidationError('username "%s" is already in use.' % username)
