from django.contrib import messages  # TODO - FBV
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from callisto.main_app.models import Post
from callisto.users_app.models import AppUser

from callisto.users_app.forms import UserUpdateForm, ProfileUpdateForm


class PostListView(views.ListView):
    model = Post
    template_name = 'main/blog.html'
    ordering = ['-date_posted', ]
    paginate_by = 5


class UserPostListView(views.ListView):
    model = Post
    template_name = 'main/user_posts.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(AppUser, email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(views.DetailView):
    model = Post
    template_name = 'main/post_detail.html'


class PostCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'main/post_create.html'

    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'main/post_update.html'
    success_url = reverse_lazy('blog')

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


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'main/profile.html', context)
