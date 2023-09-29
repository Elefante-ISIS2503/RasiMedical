from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profesional


@csrf_exempt
def submitDoctor(request):
    if request.method == "POST":
        print("SUBMITTING DOCTOR...")

        nombre = request.POST.get("nombre")
        username = request.POST.get("username")
        password = request.POST.get("password")
        cedula = request.POST.get("cedula")
        correo = request.POST.get("correo")
        fecha_nacimiento = request.POST.get("fechaNacimiento")
        rol = request.POST.get("rol")
        especialidad = request.POST.get("especialidad")

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


def getDoctors(request):
    profesionales = Profesional.objects.order_by("id").reverse()[:5]

    print("PROFESIONALES:")

    for profesional in profesionales:
        print(profesional)

    data = {"profesionales": list(profesionales.values())}
    return JsonResponse(data)

def healthCheck(request):
    return HttpResponse('ok')
