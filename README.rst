==================
gyazowinpsvr
==================

gyazowin+ のサーバ－、python + Django実装です。



Requirement
--------------

:Python: 3.6以上
:Django: 2.0以上


Quick start
-----------
1. インストールする::

    pip install -U https://github.com/wiredforest/gyazowinpsvr/archive/master.tar.gz

2. settings.pyのINSTALLED_APPSに足す::

    INSTALLED_APPS = [
        ...
        'gyazosvr',  # add
        'django.contrib.sites',
        'django.contrib.sitemaps',
    ]

    SITE_ID = 1  # add

3. MEDIA_ROOT、MEDIA_URLを設定する::

    # settings.py
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

4. ルートのurls.pyに足す::

	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
	    url(r'^gya/', include('gyazosvr.urls')),  # add
	]

5. python manage.py migrate　でモデルを追加する.

6. python manage.py runserver 等で動かし、gyazowin+側の設定を施した上で、アップロードする。

7. MEDIA_ROOTにファイルが保存されていれば動作しています。

