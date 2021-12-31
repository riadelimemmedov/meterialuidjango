from django import forms
from django.db.models.fields import DateTimeField
from django.core.exceptions import ValidationError
from .models import Preference

class PreferenceModelForm(forms.ModelForm):
    some_date =  forms.DateField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    class Meta:
        model = Preference
        fields = '__all__'
    
    #!Bio alani ucun ayrilmis xeta yeri
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) < 10:
            raise ValidationError('The bio is too short')

        return bio
    
    def clean_first_name(self):
            name = self.cleaned_data.get('first_name')
            if len(name) < 2:
                raise ValidationError('The bio is too short')

            return name
