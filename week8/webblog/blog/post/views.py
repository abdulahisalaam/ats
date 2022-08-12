from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages


from .forms import PostForm, CommentForm
from .mixins import AjaxFormMixin
from .models import Post, Comment


# Create your views here.
class UserSignup(CreateView):
        model = User
        fields = ['username', 'password','email']
        template_name ='registration/signup.html'
        

class HomeView(ListView):
    model = Post
    template_name = 'post/home.html'
    paginate_by = 2
    

class PostView(DetailView):
    model = Post
    template_name = 'post/post_details.html'


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/add_post.html'
    success_url = '/home/'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update_post.html' 
    success_url = reverse_lazy('home')


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post/delete_post.html'    

    
class PostList(ListView):
    model = Post
    # queryset = Post.active_objects.all()
    queryset = Post.delete_objects.all()
    context_object_name = 'post_list'
    # queryset = Post.objects.filter(status='published')
    #fields= '__all__'
    template_name = "index.html"


class UserUserProfileEditView(UserChangeForm):
    form_class = UserChangeForm
    template_name = 'post/Edit_profile.html'
    success_url = reverse_lazy('home')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "post/add_comment.html"
    # template_name = "post/add_comment.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        author = user.objects.filter(id=self.request.user.id).first()
        form.instance.user = author
        return super().form_valid(form)

    

    
