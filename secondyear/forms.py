from django import forms
from secondyear.models import *
from django.core import validators



class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create Password For Student'}))
    class Meta:
        model = Student
        fields = ['rollno','name','phno','password']

        widgets = {
            'rollno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Create Roll Number'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'}),
            'phno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Student Phone Number'})

        }

    def clean_password(self):
        try:
            cleaned_data = super().clean()
            phno = cleaned_data['phno']
            password = cleaned_data['password']
            if str(password) != str(phno):
                raise forms.ValidationError('password should be same as phone number')
            else:
                return password
        except KeyError:
            raise forms.ValidationError('password should be same as validated phone number')


    def clean_phno(self):
        cleaned_data = super().clean()
        phno = cleaned_data['phno']
        if len(str(phno)) != 10:
            raise forms.ValidationError('Phonenumber should be 10 digits')
        return phno