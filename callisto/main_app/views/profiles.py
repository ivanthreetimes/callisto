from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from callisto.users_app.models import Profile


class ProfileUpdateView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    model = Profile
    fields = "__all__"
    template_name = 'main/profile.html'
    success_url = reverse_lazy('profile')

    # TODO - send success_message

    def get_object(self, queryset=None):
        return self.request.user.profile

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
