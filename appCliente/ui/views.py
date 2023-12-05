from django.shortcuts import render
import requests
import smtplib
import ssl
from email.message import EmailMessage
from django.http import HttpResponseBadRequest, HttpResponse
from appCliente.auth0backend import getRole


# Define email sender and receiver
email_sender = "juanescoro2010@gmail.com"
email_password = "ttqk iuom assp admu"
email_receiver = "j.coronel@uniandes.edu.co"


# IP DEL BROKER:
kong_ip = "10.128.0.22:8000"


def home(request):
    return render(request, "ui/home.html")


def newDoctor(request):
    return render(request, "ui/newDoctor.html")


def newInventario(request):
    return render(request, "ui/newInventario.html")


def newSede(request):
    return render(request, "ui/newSede.html")


def submitSede(request):
    print("Guardando sede...")

    nombre = request.POST.get("nombre")
    direccion = request.POST.get("direccion")
    telefono = request.POST.get("telefono")
    ciudad = request.POST.get("ciudad")
    medicos = request.POST.get("medicos")

    if not all([nombre, direccion, telefono, ciudad, medicos]):
        return HttpResponseBadRequest("Invalid input: All fields are required")

    # take the string medicos which will be a string like "1,2,3,4,5" and convert it to a list of strings
    medicos = medicos.split(",")

    forumDict = {
        "name": nombre,
        "address": direccion,
        "phone": telefono,
        "city": ciudad,
        "medics": medicos,
    }

    print(forumDict)

    url = f"http://{kong_ip}/sedes/"
    response = requests.post(url, json=forumDict)

    if response.status_code == 201:
        return render(request, "ui/submitSede.html", forumDict)
    else:
        return render(request, "ui/submitSedeFail.html", forumDict)


def submitDoctor(request):
    print("Guardando profesional...")

    nombre = request.POST.get("nombre")
    username = request.POST.get("username")
    password = request.POST.get("password")
    cedula = request.POST.get("cedula")
    correo = request.POST.get("correo")
    fecha_nacimiento = request.POST.get("fechaNacimiento")
    rol = request.POST.get("rol")
    especialidad = request.POST.get("especialidad")

    # Basic input validation
    if not all(
        [
            nombre,
            username,
            password,
            cedula,
            correo,
            fecha_nacimiento,
            rol,
            especialidad,
        ]
    ):
        return HttpResponseBadRequest("Invalid input: All fields are required")

    forumDict = {
        "nombre": nombre,
        "username": username,
        "password": password,
        "cedula": cedula,
        "correo": correo,
        "fechaNacimiento": fecha_nacimiento,
        "rol": rol,
        "especialidad": especialidad,
    }

    print(forumDict)

    url = f"http://{kong_ip}/saveDoctor"
    response = requests.post(url, json=forumDict)

    if response.status_code == 200:
        return render(request, "ui/submitDoctor.html", forumDict)
    else:
        return render(request, "ui/submitDoctorFail.html", forumDict)


def getDoctors(request):
    role = getRole(request)
    if role == None:
        return render(request, "ui/unauthenticatedUser.html")
    
    elif role == "Doctor" or role == "Admin":
        url = f"http://{kong_ip}/postDoctors"
        response = requests.get(url)

        if response.status_code == 200:
            print("Profesionales:")

            for profesional in response.json()["profesionales"]:
                print(profesional)

            return render(request, "ui/getDoctors.html", response.json())
        else:
            print("RESPUESTA FALLIDA")

            # Enviar correo de advertencia
            subject = "SE ACABA DE CAER UN SERVICIO EN RASI MEDICAL (USUARIOS)!"
            body = """
            HOLY MACARRONI: OJO PUES SE MURIO EL MANEJADOR DE USUARIOS.
            """

            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            return render(request, "ui/doctorNoDisp.html", response.json())
    else:
        return HttpResponse("Unauthorized Access")


def getDoctorsBySede(request, sede_id):
    print("Buscando doctores por sede...")
    url = f"http://{kong_ip}/sedes/{sede_id}/doctors"
    response = requests.get(url)
    

    if response.status_code == 200:
        print("Doctores:")

        response = response.json()

        for doctor in response:
            print(doctor)

        print({"profesionales": response, "sede_id": sede_id})

        return render(
            request,
            "ui/getDoctorsBySede.html",
            {"profesionales": response, "sede_id": sede_id},
        )
    else:
        print("RESPUESTA FALLIDA")

        # Enviar correo de advertencia
        subject = "SE ACABA DE CAER UN SERVICIO EN RASI MEDICAL (DOCTORES)!"
        body = """
        HOLY MACARRONI: OJO PUES SE MURIO EL MANEJADOR DE DOCTORES.
        """

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return render(request, "ui/doctorNoDisp.html", response.json())


def getSedes(request):
    print("Buscando sedes...")
    url = f"http://{kong_ip}/sedes/"
    response = requests.get(url)

    # print(response.json())

    if response.status_code == 200:
        print("Sedes:")

        response = response.json()

        for sede in response:
            # replace the name of the _id field with id
            sede["id"] = sede.pop("_id")
            # replace the medics field with a comma separated string of the medic ids
            sede["medics"] = ",".join(sede["medics"])
            print(sede)

        return render(request, "ui/getSedes.html", {"sedes": response})
        print("RESPUESTA FALLIDA")

        # Enviar correo de advertencia
        subject = "SE ACABA DE CAER UN SERVICIO EN RASI MEDICAL (SEDES)!"
        body = """
        HOLY MACARRONI: OJO PUES SE MURIO EL MANEJADOR DE SEDES.
        """

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return render(request, "ui/sedeNoDisp.html", response.json())


def submitInventario(request):
    print("Guardando recurso...")

    # Get data from the form
    nombre = request.POST.get("nombre")
    cantidad = request.POST.get("cantidad")
    tipo = request.POST.get("tipo")
    descripcion = request.POST.get("descripcion")
    proveedor = request.POST.get("proveedor")

    if not all([nombre, cantidad, tipo, descripcion, proveedor]):
        return HttpResponseBadRequest("Invalid input: All fields are required")

    forumDict = {
        "nombre": nombre,
        "cantidad": cantidad,
        "tipo": tipo,
        "descripcion": descripcion,
        "proveedor": proveedor,
    }

    print(forumDict)

    url = f"http://{kong_ip}/saveInventario"

    response = requests.post(url, json=forumDict)

    if response.status_code == 200:
        return render(request, "ui/submitInventario.html", forumDict)
    else:
        return render(request, "ui/submitInventarioFail.html", forumDict)


def InventarioSearchFront(request):
    print("Buscando recurso...")

    nombre = request.POST.get("nombre")

    if not nombre:
        return HttpResponseBadRequest("Invalid input: nombre is required")

    forumDict = {"nombre": nombre}

    print(forumDict)

    url = f"http://{kong_ip}/searchInventario"

    response = requests.post(url, json=forumDict)

    if response.status_code == 200:
        return render(request, "ui/InventarioSearchFront.html", response.json())
    else:
        return render(request, "ui/InventarioSearchFrontFail.html", forumDict)


def getInventario(request):
    
    url = f"http://{kong_ip}/postInventarios"
    response = requests.get(url)

    if response.status_code == 200:
        print("INVENTARIO:")

        for recurso in response.json()["recursos"]:
            print(recurso)

        return render(request, "ui/getInventario.html", response.json())
    else:
        print("RESPUESTA FALLIDA")

        # Enviar correo de advertencia
        subject = "SE ACABA DE CAER UN SERVICIO EN RASI MEDICAL (INVENTARIO)!"
        body = """
        HOLY MACARRONI: OJO PUES SE MURIO EL MANEJADOR DE INVENTARIO.
        """

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return render(request, "ui/inventarioNoDisp.html", response.json())
