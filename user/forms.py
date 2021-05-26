
from django import forms
from django.core import validators
from user.models import userdata, feedback


def name_check(value):
    if value.isalpha()!=True:
        raise forms.ValidationError("only strings are allowed")



class userForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,validators=[name_check])
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(), required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    def __str__(self):
        return self.mail


    class Meta:
        model=userdata
        fields=['name','passwd','cwpasswd','mail','mobileno','qualification','status']
    def clean(self):
        cleaned_data=super().clean()
        inputpasswd=cleaned_data['passwd']
        inputcwpasswd=cleaned_data['cwpasswd']
        if inputpasswd!=inputcwpasswd:
            raise forms.ValidationError("password should be match")



class feedbackform(forms.ModelForm):
    bookname = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    booktype = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    bookprice = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    #file = forms.FileField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    rating = forms.ChoiceField(choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    review = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    class Meta:
        model = feedback
        fields = ('bookname', 'booktype', 'bookprice','rating','review')