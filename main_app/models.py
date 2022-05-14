import resource
from django.db import models
from django.urls import reverse
# Create your models here.

DEPOSITS = (
  ('Mg', 'Magnesium'), ('Al', 'Aluminium'),
  ('Ti', 'Titanium'), ('Fe', 'Iron'),
  ('Cu', 'Copper'), ('W', 'Tungsten'),

)

class Resource(models.Model):
  mineral = models.CharField(max_length=2, choices=DEPOSITS)

  def __str__(self):
    return self.get_mineral_display()

  def get_absolute_url(self):
    return reverse('resource_detail', kwargs={'pk': self.id})

class Planet(models.Model):
  name = models.CharField(max_length=20)
  namesake = models.CharField(max_length=100)
  orbital_period = models.FloatField()
  description = models.TextField(max_length=500)

  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'planet_id': self.id})
  
  resources = models.ManyToManyField(Resource)

class Moon(models.Model):
  name = models.CharField(max_length=20)
  namesake = models.CharField(max_length=100)
  orbital_period = models.FloatField(default=0)
  description = models.TextField(max_length=500)

  planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} ({self.id})"


