from django.urls import path

from callisto.main_app.views.generic import AboutView
from callisto.main_app.views.profiles import ProfileUpdateView
from callisto.main_app.views.posts import PostListView, UserPostListView, \
    PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('<str:email>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
