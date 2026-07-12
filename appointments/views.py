from django.shortcuts import get_object_or_404, redirect, render
from .forms import AppointmentForm
from .models import Appointment


def home(request):
    action = request.GET.get("action")
    appointment = None
    form = None

    if action == "add":
        form = AppointmentForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("appointments_home")
    elif action == "edit":
        appointment = get_object_or_404(Appointment, pk=request.GET.get("id"))
        form = AppointmentForm(request.POST or None, instance=appointment)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("appointments_home")
    elif action == "delete":
        appointment = get_object_or_404(Appointment, pk=request.GET.get("id"))
        appointment.delete()
        return redirect("appointments_home")

    appointments = Appointment.objects.select_related("patient", "doctor").all()
    return render(request, "appointments/index.html", {"appointments": appointments, "form": form, "appointment": appointment})
