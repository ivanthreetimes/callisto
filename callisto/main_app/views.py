from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

posts = [
    {
        'author': 'Ivan',
        'title': 'Data Science',
        'content': 'Pandas',
        'date_posted': 'August 28, 2021',
    },
    {
        'author': 'Petar',
        'title': 'Machine Learning',
        'content': 'scikit-learn',
        'date_posted': 'August 28, 2021',
    },
]


class IndexView(views.TemplateView):
    template_name = 'main/index.html'

    # @method_decorator(login_required(login_url=reverse_lazy('user login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {
            'posts': posts,
        }
        return context


class AboutView(views.TemplateView):
    template_name = 'main/about.html'
