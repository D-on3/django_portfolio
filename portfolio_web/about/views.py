from django.shortcuts import render, redirect
from .models import AboutMe, Project
from .forms import AboutMeForm

def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'about/about.html', {'about': about})

def edit_about_me(request):
    about = AboutMe.objects.first()
    if request.method == 'POST':
        form = AboutMeForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutMeForm(instance=about)
    return render(request, 'about/edit_about.html', {'form': form, 'about': about})
