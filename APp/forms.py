from django import forms
from APp.models import *
# Create your forms here.
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','pic']

class TopicForm(forms.ModelForm):
    class Meta:
        model =Topic
        fields='__all__'

class PageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url']

class RecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields=['date','author']
        