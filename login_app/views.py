from django.shortcuts import render
from django.http import JsonResponse
from .models import User
import json

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        password = data['password']


        user, created = User.objects.get_or_create(email=email, defaults={'name': name, 'password': password})

        if created:
            return JsonResponse({'success': True, 'name': user.name})
        else:
            return JsonResponse({'success': False, 'message': 'User already exists'}, status=400)

    return render(request, 'login_form.html')

def welcome_view(request, name):
    return render(request, 'welcome.html', {'name': name})
