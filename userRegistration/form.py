from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import CustomUser,MyForm
from django.core.validators import RegexValidator
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import re

class userRegistrationForm(UserCreationForm):
   # password = forms.CharField(widget=forms.PasswordInput)
   # confirm_password = forms.CharField(widget=forms.PasswordInput)
   class Meta :
    model = CustomUser
    fields =('registration_no','email','password')
   
   def clean(self):
        cleaned_data = super(userRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        # confirm_password = cleaned_data.get('confirm_password')
        # if password != confirm_password:
        #     raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class userLoginForm(forms.ModelForm):
      class Meta:
        model = CustomUser
        fields = ('registration_no','password')
      def clean(self):
         if self.is_valid():
            registration_no = self.cleaned_data['registration_no']
            password = self.cleaned_data['password']

            if not authenticate(registration_no=registration_no,password=password):
               raise forms.ValidationError('please provide registration no and password')
               
         



class MyUserForm(forms.ModelForm):
    # Validations
    name = forms.CharField(label='Name', max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name',
        'style'  :'font-size:13px, text-transform : capitalized' }))
    department = forms.CharField(label='Department', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Department Name'}))
    session = forms.CharField(label='Session', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Session'}))
    registration_number = forms.CharField(label='Registration Number', max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Registration Number'}))
    hall = forms.CharField(label='Hall', max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Your Hall Name'}))
    email = forms.CharField(label='Email', max_length=100,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    fathers_name = forms.CharField(label='Fathers_name', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Hall Name'}))
    mothers_name = forms.CharField(label='mothers_name', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Hall Name'}))
    present_address = forms.CharField(label='Present_Address', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter Your Present Address'}))
    permanent_address = forms.CharField(label='Permanent_Address', max_length=100,
                                      widget=forms.TextInput(attrs={'placeholder': 'Enter Your Permanent Address'}))
    contact_no = forms.CharField(label='Contact_Number', max_length=20, validators=[
        RegexValidator(
            r'^(?:\+88)?01[3-9]\d{8}$', message="Enter a valid phone number starting with +8801")
    ], widget=forms.TextInput(attrs={'placeholder': 'Enter Contact Number such as +8801xxxxxxx'}))

    def clean_contact_no(self):
            contact_no = self.cleaned_data['contact_no']
            # Remove any non-digit characters from the contact number
            contact_no = re.sub(r'\D', '', contact_no)
            # Check if the number starts with +88 and remove it if present
            if contact_no.startswith('88') and len(contact_no) > 10:
                  contact_no = contact_no[2:]
            # Add the "01" prefix to the contact number
            contact_no =  contact_no
            return contact_no

    def clean(self):
            cleaned_data = super().clean()
            # Perform any other form-wide validation if needed
            return cleaned_data
    class Meta:
        
        model = MyForm
        fields = ['image',
                  'name',
                  'department',
                  'session',
                  'registration_number',
                  'hall',
                  'email',
                  'fathers_name',
                  'mothers_name',
                  'present_address',
                  'permanent_address',
                  'contact_no',
                  'blood_group',
                  'gender',
                  'social_media_link_1',
                  'social_media_link_2',
                  'ssc_institution',
                  'ssc_board',
                  'ssc_passing_year',
                  'hsc_institution',
                  'hsc_board',
                  'hsc_passing_year',
                  'Extra_CurriCular_Activities',
                  'hobbies_interest',
                  'why_join_duits',
                  'information_tech_interest',
                  'other_club_member',
                  'skillsets']
        def __init__(self,*args,**kwargs):
           super(MyUserForm,self).__init__(*args,**kwargs)
