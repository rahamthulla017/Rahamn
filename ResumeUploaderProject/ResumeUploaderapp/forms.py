from django import forms
from ResumeUploaderapp.models import Resume, STATE_CHOICES

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

CITY_CHOICES = [
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
    ('Pune', 'Pune'),
    ('Delhi', 'Delhi'),
    ('Bangalore', 'Bangalore')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    state = forms.ChoiceField(label='State', choices=STATE_CHOICES, widget=forms.Select)

    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'Pin Code',
            'address': 'Address',
            'mobile': 'Mobile Number',
            'profile_image': 'Profile Image',
            'my_file': 'Document',
            'email': 'Email Id'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
