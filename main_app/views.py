from django.shortcuts import render
from .models import Planet

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def planets_index(request):
  planets = Planet.objects.all()
  return render(request, 'planets/index.html', { 'planets': planets })

def planets_detail(request, planet_id):
  planet = Planet.objects.get(id=planet_id)
  return render(request, 'planets/detail.html', { 'planet': planet })