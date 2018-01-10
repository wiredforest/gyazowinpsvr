import os
import hashlib
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.views.defaults import bad_request


class GyazoSvrIndexView(generic.TemplateView):
    template_name = 'gyazosvr/index.html'


class Upload(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        return bad_request(request, Exception())
        # return HttpResponse("POSTで送ってくんなましー")

    def post(self, request, *args, **kwargs):
        file_id = request.POST.get('id', None)
        if not file_id:
            ip = request.META.get('REMOTE_ADDR', 'N/A')
            seed = "{}{}".format(ip, timezone.now().timestamp())
            file_id = hashlib.md5(seed.encode()).hexdigest()

        up_dir = os.path.join(settings.MEDIA_ROOT, 'up')
        if not os.path.exists(up_dir):
            os.mkdir(up_dir)
        file_name = file_id + '.png'
        with open(os.path.join(up_dir, file_name), 'wb') as dest:
            for chunk in request.FILES['imagedata'].chunks():
                dest.write(chunk)

        host = settings.GYAZOWINPSVR_HOST
        return HttpResponse("http://{}/view/{}".format(host, file_name))
