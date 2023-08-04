from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def perfil_view(request):
    # Lógica de la vista de perfil del usuario
    return render(request, 'usuario/perfil.html')
from django.shortcuts import render

# Create your views here.
