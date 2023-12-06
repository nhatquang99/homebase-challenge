from django.shortcuts import render
from django.views import generic
import requests
    
def user_list(request):
    api_url = 'http://127.0.0.1:5001/api/users'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        users = response.json()
        return render(request, 'user_list.html', {'users': users})

    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error_message': f'Error: {e}'})

