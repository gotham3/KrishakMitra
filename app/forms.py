from django import forms
from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name..'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name..'}))
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField(label='Zip')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Last Name..','rows' : 5, 'cols' :20}))
    class Meta:
        model = UserProfile
        fields = ('email','username','first_name','last_name','address','city','state','zip','description',)
