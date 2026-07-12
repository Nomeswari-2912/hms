from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "date_of_birth", "contact_number"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }
