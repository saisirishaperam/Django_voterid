from django import forms
from app1.models import vote
from datetime import date
import random
import string

class voter_form(forms.ModelForm):

    class Meta:
        model = vote
        fields = ('name','gender','date_of_birth','address','image')

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


    # # Generate unique voter ID
    # if not instance.voter_id:
    #     while True:
    #         random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    #         if not vote.objects.filter(voter_id=random_id).exists():
    #             instance.voter_id = random_id
    #             break

    # if commit:
    #     instance.save()
    # return instance