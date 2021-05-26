
from django import forms
from django.core import validators

from bookvendor.models import bookvendor, upload


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only strings are allowed")



class bookvendorForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    location = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.mail


    class Meta:
        model = bookvendor
        fields=['name','passwd','cwpasswd','mail','mobileno','location','status']
    def clean(self):
        cleaned_data=super().clean()
        inputpasswd=cleaned_data['passwd']
        inputcwpasswd=cleaned_data['cwpasswd']
        if inputpasswd!=inputcwpasswd:
            raise forms.ValidationError("password should be match")



class UploadfileForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ('filename','filetype','fileprice','file')