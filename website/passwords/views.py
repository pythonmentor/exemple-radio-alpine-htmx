from django.views.generic import TemplateView


class PassswordHomeView(TemplateView):
    template_name = 'passwords/index.html'
