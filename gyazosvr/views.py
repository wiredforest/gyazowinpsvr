from django.views import generic


class GyazoSvrIndexView(generic.TemplateView):
    template_name = 'gyazosvr/index.html'
