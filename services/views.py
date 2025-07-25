from django.http import JsonResponse
from .models import Service

def service_list(request):
    services = Service.objects.all().values()
    return JsonResponse(list(services), safe=False)
