from django import forms
#from data.models import Person

class PersonForm(forms.Form):
    picture = forms.ImageField(label="Picture:")
    firstname = forms.CharField(label="FirstName:")
    lastname = forms.CharField(label="LastName:")
    """class Meta:
        model = Person
        fields = ('picture', 'firstname', 'lastname', )"""


class ProjectForm(forms.Form):
    title = forms.CharField(label="Título", required=True)
    description = forms.CharField(label="Descripción", required=True)
    image = forms.ImageField(label="Imagen", required=True)
    link = forms.URLField(label="Dirección Web", required=True)