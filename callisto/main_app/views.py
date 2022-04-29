from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from callisto.main_app.models import Post


class PostListView(views.ListView):
    model = Post
    template_name = 'main/blog.html'
    ordering = ['-date_posted', ]
    paginate_by = 5


class PostDetailView(views.DetailView):
    model = Post
    template_name = 'main/post_detail.html'


class PostCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'main/post_create.html'

    # success_url = reverse_lazy('blog') # Currently uses get_absolute_url in models

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'main/post_update.html'

    # success_url = reverse_lazy('blog') # Currently uses get_absolute_url in models

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    model = Post
    template_name = 'main/post_confirm_delete.html'
    success_url = reverse_lazy('blog')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AboutView(views.TemplateView):
    template_name = 'main/about.html'
