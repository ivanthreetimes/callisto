from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


class IndexView(views.TemplateView):
    template_name = 'index.html'

    # @method_decorator(login_required(login_url=reverse_lazy('user login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
