from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

User = get_user_model()


def home(request):
    message = None
    if request.user.is_authenticated:
        message = f"You are already logged in as {request.user.username}."
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip().replace(" ", "")
        user = authenticate(request, username=name, password=phone)
        if user is not None:
            login(request, user)
            return redirect("home")
        message = "Invalid name or phone number. Use your registered name and phone number with +91 or +1."

    return render(request, "accounts/home.html", {"message": message})


def register(request):
    message = None
    name = ""
    phone = ""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip().replace(" ", "")
        if not name or not phone:
            message = "Name and phone number are required."
        elif not (phone.startswith("+91") or phone.startswith("+1")):
            message = "Phone number must start with +91 or +1."
        elif User.objects.filter(username=name).exists():
            message = "A user with that name already exists."
        else:
            user = User.objects.create_user(username=name, password=phone)
            login(request, user)
            return redirect("home")
    return render(request, "accounts/register.html", {"message": message, "name": name, "phone": phone})


def logout_view(request):
    logout(request)
    return redirect("accounts_home")
