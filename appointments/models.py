from django.db import models


class Appointment(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date} at {self.time}"
