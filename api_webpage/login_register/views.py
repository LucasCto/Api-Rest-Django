from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.crypto import get_random_string


# Create your views here.

User = get_user_model()

def register(request):
    if request.method == 'POST':
        # Procesar el formulario de registro y guardar al usuario en la base de datos
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=email, email=email, password=password)

        # Generar y asignar el token de acceso al usuario
        token = get_random_string(length=32)
        user.access_token = token
        user.save()

        # Enviar el correo electrónico con el enlace de activación
        send_mail(
            'Token de acceso',
            f'Guarda el siguiente codigo que es necesario para acceder a tu cuenta {token}',
            'noreply@example.com',
            [email],
            fail_silently=False,
        )

        return render(request, 'registration/success.html')

    return render(request, 'registration/register.html')
