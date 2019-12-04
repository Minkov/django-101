from django import forms

from django101.models.superhero import Superhero


class SuperheroCreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    secret_identity = forms.CharField(label='Secret Identity', max_length=30, widget=forms.PasswordInput())

    def save(self):
        name = self.cleaned_data['name']
        secret_identity = self.cleaned_data['secret_identity']
        superhero = Superhero(name=name, secret_identity=secret_identity)
        superhero.save()
