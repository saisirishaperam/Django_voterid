from django import forms
from app1.models import vote
from datetime import date
import random
import string

class voter_form(forms.ModelForm):

    class Meta:
        model = vote
        fields = ('name','gender','date_of_birth','aadhar','address','image')

        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date'
            })
        }


    # Custom validation for age
    def clean(self):
        cleaned_data = super().clean()
        dob = cleaned_data.get('date_of_birth')

        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            if age < 18:
                raise forms.ValidationError("Age should be greater than or equal to 18.")

            cleaned_data['age'] = age

        return cleaned_data

