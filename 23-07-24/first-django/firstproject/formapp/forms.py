from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2100))
    )
    gender = forms.ChoiceField(
        choices=[("M", "Male"), ("F", "Female")], widget=forms.RadioSelect
    )
    country = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    agree_to_terms = forms.BooleanField()
