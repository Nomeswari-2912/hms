from django.shortcuts import get_object_or_404, redirect, render
from .forms import DoctorForm
from .models import Doctor


def home(request):
    action = request.GET.get("action")
    doctor = None
    form = None

    if action == "add":
        form = DoctorForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("doctors_home")
    elif action == "edit":
        doctor = get_object_or_404(Doctor, pk=request.GET.get("id"))
        form = DoctorForm(request.POST or None, instance=doctor)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("doctors_home")
    elif action == "delete":
        doctor = get_object_or_404(Doctor, pk=request.GET.get("id"))
        doctor.delete()
        return redirect("doctors_home")

    doctors = Doctor.objects.all()
    return render(request, "doctors/index.html", {"doctors": doctors, "form": form, "doctor": doctor})
