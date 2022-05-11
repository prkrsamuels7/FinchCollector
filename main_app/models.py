from django.db import models

# Create your models here.

class Planet(models.Model):
  name = models.CharField(max_length=20)
  namesake = models.CharField(max_length=100)
  orbital_period = models.FloatField()
  description = models.TextField(max_length=500)

  def __str__(self):
    return f"{self.name} ({self.id})"
