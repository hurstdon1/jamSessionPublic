from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Field
from .models import Profile

class UserCreateForm(UserCreationForm):
    
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class ProfileUpdateForm(forms.ModelForm):

    
    class Meta:
        model = Profile
        fields = (
            "avatar",
            "instruments",
            "singer",
            "experience_level",
            "goals",
            "music_production_experience",
            "location",
            "location_zip",
            "associated_acts",
            "profile_text",
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["instruments"].label = "What instruments do you play?"
        self.fields['instruments'].widget.attrs.update(style='max-height: 8em')
        self.fields["singer"].label = "Do you sing?"
        self.fields["experience_level"].label = "Experience Level"
        self.fields["goals"].label = "What are your goals?"
        self.fields['goals'].widget.attrs.update(style='max-height: 8em')
        self.fields["music_production_experience"].label = "Do you have music production experience?"
        self.fields["location"].label = "How far are you willing to travel?"
        self.fields['location'].widget.attrs.update(style='max-height: 8em')
        self.fields['location_zip'].label = "Enter your zip code"
        self.fields["associated_acts"].label = "Are you in any bands now?"
        self.fields['associated_acts'].widget.attrs.update(style='max-height: 8em')
        self.fields["profile_text"].label = "Bio"
        self.fields['profile_text'].widget.attrs.update(style='max-height: 8em')

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)