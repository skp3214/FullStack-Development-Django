from django import forms

class UserForm(forms.Form):
    first_name=forms.CharField(label='First Name',max_length=100)
    last_name=forms.CharField(label='Last Name',max_length=100)
    email=forms.EmailField(label='Email',max_length=100)
    password=forms.CharField(label='Password',widget=forms.PasswordInput())
    gender=forms.ChoiceField(choices={'1':'Male','2':'Female'},widget=forms.RadioSelect)
    country=forms.ChoiceField(choices={'1':'India','2':'USA'},widget=forms.Select)
    intrest=forms.ChoiceField(choices={'1':'Cricket','2':'Football','3':'Hockey'},widget=forms.CheckboxSelectMultiple)
    
    