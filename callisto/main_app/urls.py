from django.urls import path
from callisto.main_app.views import PostListView, AboutView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, profile

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('profile/', profile, name='profile'),
    path('<str:email>', UserPostListView.as_view(), name='user-posts'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
