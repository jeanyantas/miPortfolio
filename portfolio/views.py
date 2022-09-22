from django.shortcuts import render, redirect
from .models import Project
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["jean.yantas1@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, '¡Correo Enviado!')
        return redirect('home')