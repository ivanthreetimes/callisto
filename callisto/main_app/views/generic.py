from django.views import generic as views


class AboutView(views.TemplateView):
    template_name = 'main/about.html'
