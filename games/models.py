from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)  # Name of the game
    description = models.TextField()         # Short description
    rules = models.TextField()               # Rules of the game

    def __str__(self):
        return self.name
