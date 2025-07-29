from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPost
from .forms import BlogPostForm

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog_form.html'
    success_url = reverse_lazy('blog_list')
    login_url = reverse_lazy('login')  # Redirect to login if not logged in


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('blog_list')
        return render(request, 'signup.html', {'form': form})
