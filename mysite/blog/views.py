from re import template
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .forms import PostForm
from .models import Comentario, Post

# Create your views here.
# class Home(generic.TemplateView):
#     template_name = "blog/posts.html"

def post_list(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)


def post_detail(request,pk ):
    post = Post.objects.get(pk=pk)
    comentario = Comentario.objects.filter(autor = post.autor)
    context = {
        'post': post,
        'comentarios' : comentario
    }
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    form = PostForm
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
        pass
    else:
        pass

    return render(request, 'blog/post_edit.html', {'form':form})
