from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Recurso


@csrf_exempt
def submitInventario(request):
    if request.method == "POST":
        print("Submit Inventario")

        nombre = request.POST.get("nombre")
        cantidad = request.POST.get("cantidad")
        tipo = request.POST.get("tipo")
        descripcion = request.POST.get("descripcion")
        proveedor = request.POST.get("proveedor")

        recurso = Recurso(
            nombre=nombre,
            cantidad=cantidad,
            tipo=tipo,
            descripcion=descripcion,
            proveedor=proveedor,
        )

        print(recurso)

        recurso.save()

        return JsonResponse({"message": "Recurso creado exitosamente"})
    else:
        return JsonResponse({"message": "Método no permitido"})


def getInventario(request):
    recursos = Recurso.objects.order_by("id").reverse()[:5]

    print("Recursos: ")

    for recurso in recursos:
        print(recurso)

    data = {"recursos": list(recursos.values())}
    return JsonResponse(data)


def healthCheck(request):
    return HttpResponse("ok")
