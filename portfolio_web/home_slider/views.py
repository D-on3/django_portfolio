from django.shortcuts import render
from .models import SliderImage

def slider(request):
    images = SliderImage.objects.all()
    return render(request, 'home_slider/slider.html', {'images': images})