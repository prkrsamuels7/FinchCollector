from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Planet, Resource
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
  return render(request, 'planets/detail.html', { 'planet': planet, 'moon_form': moon_form })

def add_moon(request, planet_id):
  form = MoonForm(request.POST)
  if form.is_valid():
    new_moon = form.save(commit=False)
    new_moon.planet_id = planet_id
    new_moon.save()
  return redirect('detail', planet_id=planet_id)


class PlanetCreate(CreateView):
  model = Planet
  fields = '__all__'

class PlanetUpdate(UpdateView):
  model = Planet
  fields = ['namesake', 'orbital_period', 'description']

class PlanetDelete(DeleteView):
  model = Planet
  success_url = '/planets/'

class ResourceList(ListView):
  model = Resource

class ResouceDetail(DetailView):
  model = Resource

class ResourceCreate(CreateView):
  model = Resource
  fields = '__all__'

class ResourceUpdate(UpdateView):
  model = Resource
  fields = '__all__'

class ResourceDelete(DeleteView):
  model = Resource
  success_url = '/resource/'

