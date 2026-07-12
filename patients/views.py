from django.shortcuts import get_object_or_404, redirect, render
from .forms import PatientForm
from .models import Patient


def home(request):
    action = request.GET.get("action")
    patient = None
    form = None

    if action == "add":
        form = PatientForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("patients_home")
    elif action == "edit":
        patient = get_object_or_404(Patient, pk=request.GET.get("id"))
        form = PatientForm(request.POST or None, instance=patient)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("patients_home")
    elif action == "delete":
        patient = get_object_or_404(Patient, pk=request.GET.get("id"))
        patient.delete()
        return redirect("patients_home")

    patients = Patient.objects.all()
    return render(request, "patients/index.html", {"patients": patients, "form": form, "patient": patient})
