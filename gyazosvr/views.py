import os
import hashlib
import logging
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.views.defaults import bad_request

log = logging.getLogger(__name__)


class GyazoSvrIndexView(generic.TemplateView):
    template_name = 'gyazosvr/index.html'


class Upload(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        return bad_request(request, Exception("not allowed GET request"))

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

        if 'imagedata' not in request.FILES:
            return bad_request(request, Exception("no parameter: imagedata"))

        with open(os.path.join(up_dir, file_name), 'wb') as dest:
            for chunk in request.FILES['imagedata'].chunks():
                dest.write(chunk)

        host = settings.GYAZOWINPSVR_HOST
        view_url = "http://{}/view/{}".format(host, file_name)
        log.info("[UPLOADED] {}".format(view_url))

        return HttpResponse(view_url)
