from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    def clean_esal(self):
        inputroll = self.cleaned_data['roll']
        if inputroll<1:
            raise forms.ValidationError('Minimum allowed Roll No. is 1.')
        return inputroll

    class Meta:
        model = Student
        fields = '__all__'
