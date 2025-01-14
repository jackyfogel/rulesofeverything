from django.shortcuts import render
from .models import Game

def home(request):
    context = {
        'games': Game.objects.all()  # Fetch all games from the database
    }
    return render(request, 'home.html', context)
