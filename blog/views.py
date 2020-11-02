from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post  

def login(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')
        return redirect('index')
    else:
        return render(request, 'blog/login.html')
    return render(request, 'blog/login.html')        

def index(request):
    return render(request, 'blog/index.html')

#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})
