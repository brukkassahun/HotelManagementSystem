from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as USER
from .models import User


# Create your forms here.

class NewUserForm(forms.ModelForm):
   # specify the name of model to use
    class Meta:
        model = User
        fields = '__all__'
        widgets={
			'name':forms.TextInput(attrs={'required':True,'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mb-5'}),
			'email':forms.TextInput(attrs={'required':True,'type':"email",'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 mb-5'}),
			'password':forms.TextInput(attrs={'required':True,'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
		}
    def clean_name(self):
        name = self.data['name']
        if USER.objects.filter(username=name).count() != 0:
            # raise forms.ValidationError("username is taken")
            return "username is taken"
        return ''
    def clean_email(self):
        email = self.data['email']
        if USER.objects.filter(email=email).count() != 0:
            # raise forms.ValidationError("Email is taken")
            return "Email is taken"
        return ''
    def clean_password(self):
        password = self.data['password']
        if len(password) < 8:
            # raise forms.ValidationError("Password is too short")
            return "Password is too short"
        return ''
    def isItValid(self):
        name=self.clean_name()
        email=self.clean_email()
        password=self.clean_password()
        if name =='' and email =='' and password =='':
            return True
        return False