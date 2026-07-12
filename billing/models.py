from django.db import models


class Invoice(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_cost = models.DecimalField(max_digits=10, decimal_places=2)
    test_charges = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_status = models.CharField(max_length=100)
    issued_date = models.DateField()

    def __str__(self):
        return f"Invoice {self.id} for {self.patient}"
