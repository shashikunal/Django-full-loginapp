from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from attendanceMgnt.models import UserProfile
from registration.forms import RegistrationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True )

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
			)
def save(self , commit=True):
	user = super(RegistrationForm , self).save(commit=False)
	user.first_name = self_cleaned_data['first_name']
	user.last_name = self_cleaned_data['last_name']
	user.email=self_cleaned_data['email']
	
	if commit:
		user.save()
	return user	


# email unique
class MyRegForm(RegistrationForm):
    username = forms.CharField(max_length=254, required=False, widget=forms.HiddenInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        self.cleaned_data['username'] = email
        return email

# end of email unique


# user profile form

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = (
			'email',
			'first_name',
			'last_name',
			'password'

			)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			
			'description',
			'city',
			'phone',
			'Website',
			'image'
			)

