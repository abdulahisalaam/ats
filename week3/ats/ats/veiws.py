
from django.http import HttpResponse 

def home(request, username = 'User'):
    return HttpResponse(f"hello {username}.")

class home():
    pass