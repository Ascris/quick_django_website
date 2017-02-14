from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    nom= forms.CharField(max_length=1024)
    courriel = forms.EmailField(required = True)
    password= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('nom', 'email', 'password')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.courriel = self.cleaned_data['courriel']
        user.nom = self.cleaned_data['nom']

        if commit:
            user.save()

        return user

