from django.shortcuts import get_object_or_404, redirect, render
from .forms import InvoiceForm
from .models import Invoice


def home(request):
    action = request.GET.get("action")
    invoice = None
    form = None

    if action == "add":
        form = InvoiceForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("billing_home")
    elif action == "edit":
        invoice = get_object_or_404(Invoice, pk=request.GET.get("id"))
        form = InvoiceForm(request.POST or None, instance=invoice)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("billing_home")
    elif action == "delete":
        invoice = get_object_or_404(Invoice, pk=request.GET.get("id"))
        invoice.delete()
        return redirect("billing_home")

    invoices = Invoice.objects.select_related("patient").all()
    return render(request, "billing/index.html", {"invoices": invoices, "form": form, "invoice": invoice})
