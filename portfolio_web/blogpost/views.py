from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import ContactForm

def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    return render(request, 'blog/post_list.html', {
        'category': category,
        'categories': categories,
        'posts': posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data and send email or perform other actions
            # Here, we'll just redirect back to the contact page
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'templates/contact.html', {'form': form})

def about(request):
    # Add your logic for the about page
    return render(request, 'blog/about.html')