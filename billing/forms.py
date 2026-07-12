from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["patient", "consultation_fee", "medicine_cost", "test_charges", "total_amount", "payment_status", "issued_date"]
        widgets = {
            "issued_date": forms.DateInput(attrs={"type": "date"}),
        }
