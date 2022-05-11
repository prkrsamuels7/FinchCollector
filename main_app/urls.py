from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('planets/', views.planets_index, name='index'),
  path('planets/<int:planet_id>/', views.planets_detail, name='detail'),
]

