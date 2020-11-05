from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post  
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, 'blog/index.html')

@login_required
def galeria(request):
    return render(request, 'blog/galeria.html')


#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})
