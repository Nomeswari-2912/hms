from django.shortcuts import get_object_or_404, redirect, render
from .forms import MedicineForm
from .models import Medicine


def home(request):
    action = request.GET.get("action")
    medicine = None
    form = None

    if action == "add":
        form = MedicineForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("pharmacy_home")
    elif action == "edit":
        medicine = get_object_or_404(Medicine, pk=request.GET.get("id"))
        form = MedicineForm(request.POST or None, instance=medicine)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("pharmacy_home")
    elif action == "delete":
        medicine = get_object_or_404(Medicine, pk=request.GET.get("id"))
        medicine.delete()
        return redirect("pharmacy_home")

    medicines = Medicine.objects.all()
    return render(request, "pharmacy/index.html", {"medicines": medicines, "form": form, "medicine": medicine})
