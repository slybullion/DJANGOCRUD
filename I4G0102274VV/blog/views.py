from dataclasses import fields
from django.shortcuts import render
from .models import Post
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
class PostCreateView(generic.CreateView):
    model = Post
    fields="__all__"
    template_name = "blog/post_form.html"
    success_url: reverse_lazy("blog:all")
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
class PostUpdateView(generic.UpdateView):
    model = Post
    fields= "__all__"
    template_name = "base.html"
    success_url: reverse_lazy("blog:all")
class PostDeleteView(generic.DeleteView):
    model = Post
    fields= "__all__"
    template_name = "blog/post_confirm_delete.html"
    success_url: reverse_lazy("blog:all")
    
    


