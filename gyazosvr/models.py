from django.db import models
from django.utils.translation import ugettext_lazy as _


class ScreenShotUploadLog(models.Model):
    """ アップロードのログ """
    uploaded_on = models.DateTimeField(_('uploaded on'), auto_now_add=True)

    class Meta:
        app_label = 'gyazosvr'
        verbose_name = _('screen shot uploaded log')
        verbose_name_plural = _('screen shot uploaded logs')

    def __repr__(self):
        return ("<ScreenShotUploadLog:id={}>".
                format(self.id))

    def __str__(self):
        return self.__repr__()


class ScreenShotResource(models.Model):
    """ アップロードされたスクショのファイル情報など """
    # foreign key
    log = models.OneToOneField(ScreenShotUploadLog, on_delete=models.CASCADE)

    # fields
    file = models.ImageField(_('file'),
                             height_field='height', width_field='width')
    height = models.IntegerField(_('height'))
    width = models.IntegerField(_('width'))

    class Meta:
        app_label = 'gyazosvr'
        verbose_name = _('screen shot resource')
        verbose_name_plural = _('screen shot resources')

    # TODO: 現状、モデルが消えてもファイルは消えないよ

    def __repr__(self):
        return ("<ScreenShotResource:id={}>".
                format(self.id))

    def __str__(self):
        return self.__repr__()


class ScreenShotRemoveEvent(models.Model):
    """ 削除の履歴 """
    # foreign key
    log = models.OneToOneField(ScreenShotUploadLog, on_delete=models.CASCADE)

    # fields
    deleted_on = models.DateTimeField(_('deleted on'), auto_now_add=True)

    class Meta:
        app_label = 'gyazosvr'
        verbose_name = _('screen shot remove event')
        verbose_name_plural = _('screen shot remove events')

    # TODO: 現状、モデルが消えてもファイルは消えないよ

    def __repr__(self):
        return ("<ScreenShotRemoveEvent:id={}>".
                format(self.id))

    def __str__(self):
        return self.__repr__()

