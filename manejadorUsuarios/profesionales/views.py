from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Profesional
import json


@csrf_exempt
def saveDoctor(request):
    if request.method == "POST":
        print("Guardando profesional")
        print(json.loads(request.body))

        # nombre = request.POST.get("nombre")
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # cedula = request.POST.get("cedula")
        # correo = request.POST.get("correo")
        # fecha_nacimiento = request.POST.get("fechaNacimiento")
        # rol = request.POST.get("rol")
        # especialidad = request.POST.get("especialidad")

        data = json.loads(request.body)
        nombre = data.get("nombre")
        username = data.get("username")
        password = data.get("password")
        cedula = data.get("cedula")
        correo = data.get("correo")
        fecha_nacimiento = data.get("fechaNacimiento")
        rol = data.get("rol")
        especialidad = data.get("especialidad")

        profesional = Profesional(
            nombre=nombre,
            username=username,
            password=password,
            cedula=cedula,
            correo=correo,
            fechaNacimiento=fecha_nacimiento,
            rol=rol,
            especialidad=especialidad,
        )

        print(profesional)

        profesional.save()

        return JsonResponse({"message": "Profesional creado exitosamente"})
    else:
        return JsonResponse({"message": "Método no permitido"})


def postDoctors(request):
    profesionales = Profesional.objects.order_by("id").reverse()[:5]

    print("Profesionales: ")

    for profesional in profesionales:
        print(profesional)

    data = {"profesionales": list(profesionales.values())}
    return JsonResponse(data)


def postAllDoctors(request):
    profesionales = Profesional.objects.order_by("id").reverse()

    print("Se obtuvieron", len(profesionales), "profesionales")

    data = {"profesionales": list(profesionales.values())}
    return JsonResponse(data)


def healthCheck(request):
    return HttpResponse("ok")
