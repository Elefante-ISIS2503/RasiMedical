from django.shortcuts import render
import requests


def home(request):
    return render(request, "ui/home.html")


def newDoctor(request):
    return render(request, "ui/newDoctor.html")


def submitDoctor(request):
    print("SUBMITTING DOCTOR...")

    forumDict = {
        "nombre": request.POST.get("nombre"),
        "username": request.POST.get("username"),
        "password": request.POST.get("password"),
        "cedula": request.POST.get("cedula"),
        "correo": request.POST.get("correo"),
        "fechaNacimiento": request.POST.get("fechaNacimiento"),
        "rol": request.POST.get("rol"),
        "especialidad": request.POST.get("especialidad"),
    }

    print(forumDict)

    # Make the HTTP POST request to a specific IP address
    ip_address = "34.102.201.95:80"  # CAMBIAR ESTO A LA IP DEL BROKER
    url = f"http://{ip_address}/submitDoctor"  # CAMBIAR ESTO AL URL ENDPOINT DESEADO
    response = requests.post(url, data=forumDict)

    if response.status_code == 200:
        # do something
        pass
    else:
        # handle error
        pass

    return render(request, "ui/submitDoctor.html", forumDict)


def getDoctors(request):
    # Make the HTTP GET request to a specific IP address
    ip_address = "34.102.201.95:80"  # CAMBIAR ESTO A LA IP DEL BROKER
    url = f"http://{ip_address}/getDoctors"  # CAMBIAR ESTO AL URL ENDPOINT DESEADO
    response = requests.get(url)

    print("PROFESIONALES:")

    for profesional in response.json()["profesionales"]:
        print(profesional)

    if response.status_code == 200:
        # do something
        pass
    else:
        # handle error
        pass

    return render(request, "ui/getDoctors.html", response.json())
