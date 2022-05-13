from django.forms import ModelForm
from .models import Moon

class MoonForm(ModelForm):
  class Meta:
    model = Moon
    fields = ['name', 'namesake', 'orbital_period', 'description']