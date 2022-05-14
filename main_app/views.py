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
  id_list = planet.resources.all().values_list('id')
  resources = Resource.objects.exclude(id__in=id_list)
  moon_form = MoonForm()
  return render(request, 'planets/detail.html', { 'planet': planet, 'moon_form': moon_form, 'resources': resources })

def add_moon(request, planet_id):
  form = MoonForm(request.POST)
  if form.is_valid():
    new_moon = form.save(commit=False)
    new_moon.planet_id = planet_id
    new_moon.save()
  return redirect('detail', planet_id=planet_id)


class PlanetCreate(CreateView):
  model = Planet
  fields = ['name', 'namesake', 'orbital_period', 'description']

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
  success_url = '/resources/'

def assoc_resource(request, planet_id, resource_id):
  planet = Planet.objects.get(id=planet_id)
  planet.resources.add(resource_id)
  return redirect('detail', planet_id=planet_id)