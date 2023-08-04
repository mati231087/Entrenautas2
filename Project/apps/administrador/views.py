

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_home')
            else:
                messages.error(request,"Nombre de usuario o contraseña incorrecta.")
        else:
            messages.error(request,"Nombre de usuario o contraseña incorrecta.")
    form = AuthenticationForm()
    return render(request = request, template_name = "admin_app/login.html", context={"form":form})

