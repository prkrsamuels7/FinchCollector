from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Planet
from .forms import MoonForm

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
  moon_form = MoonForm()
  return render(request, 'planets/detail.html', {
    'planet': planet,
    'moon_form': moon_form ,
    })

class PlanetCreate(CreateView):
  model = Planet
  fields = '__all__'

class PlanetUpdate(UpdateView):
  model = Planet
  fields = ['namesake', 'orbital_period', 'description']

class PlanetDelete(DeleteView):
  model = Planet
  success_url = '/planets/'