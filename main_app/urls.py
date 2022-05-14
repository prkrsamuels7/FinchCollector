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
  path('resources/', views.ResourceList.as_view(), name='resource_index'),
  path('resources/<int:pk>/', views.ResouceDetail.as_view(), name='resource_detail'),
  path('resources/create/', views.ResourceCreate.as_view(), name='resources_create'),
  path('resources/<int:pk>/update/', views.ResourceUpdate.as_view(), name='resources_update'),
  path('resources/<int:pk>/delete/', views.ResourceDelete.as_view(), name='resources_delete'),
]

