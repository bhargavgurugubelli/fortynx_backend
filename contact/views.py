from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact
import os


@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        Contact.objects.create(name=name, email=email, message=message)
        return JsonResponse({'success': True, 'message': 'Message sent!'})

    return JsonResponse({'error': 'Only POST allowed'}, status=400)



def list_media(request):
    path = os.path.join(settings.MEDIA_ROOT, "assets")
    files = os.listdir(path) if os.path.exists(path) else []
    return JsonResponse({"files": files})