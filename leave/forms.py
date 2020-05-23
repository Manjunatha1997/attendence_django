from django import forms
from leave.models import *
from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type = "date"



class ApplyLeaveForm(forms.ModelForm):
    class Meta:
        model = ApplyLeave
        fields = ['start_date','end_date','reason']
        widgets = {
            # 'start_date' : forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'start_date' : DateInput(attrs={'class':'form-control'}),
            'end_date' : DateInput(attrs={'class':'form-control'}),

            # 'end_date' : forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'reason' : forms.Textarea(attrs={'class':'form-control','placeholder':'Type valid Reason'}),
        }


