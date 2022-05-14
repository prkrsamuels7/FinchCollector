from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('planets/', views.planets_index, name='index'),
  path('planets/<int:planet_id>/', views.planets_detail, name='detail'),
  path('planets/create/', views.PlanetCreate.as_view(), name='planets_create'),
  path('planets/<int:pk>/update/', views.PlanetUpdate.as_view(), name='planets_update'),
  path('planets/<int:pk>/delete/', views.PlanetDelete.as_view(), name='planets_delete'),
  path('planets/<int:planet_id>/add_moon/', views.add_moon, name='add_moon'),
]

