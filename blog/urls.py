from django.urls import path
from .views import BlogListView, BlogCreateView, SignUpView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', login_required(BlogCreateView.as_view()), name='blog_create'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
