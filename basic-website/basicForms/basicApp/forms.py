from django import  forms
from  django.core import validators


'''def check_for_a(value):
    if value[0].lower() !='a':
        raise forms.ValidationError("name needs to start with a")'''
        

class FormName (forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='input your email again: ')
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        
        if email != vemail:
            raise forms.ValidationError("Make sure email match!")