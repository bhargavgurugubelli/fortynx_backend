from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

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
