from django import forms
from .models import Meeting, MeetingMinutes, Resource

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'