from django.db import models
from django.urls import reverse
# Create your models here.

class Planet(models.Model):
  name = models.CharField(max_length=20)
  namesake = models.CharField(max_length=100)
  orbital_period = models.FloatField()
  description = models.TextField(max_length=500)

  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'planet_id': self.id})

class Moon(models.Model):
  name = models.CharField(max_length=20)
  namesake = models.CharField(max_length=100)
  orbital_period = models.FloatField(default=0)
  description = models.TextField(max_length=500)

  planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} ({self.id})"


