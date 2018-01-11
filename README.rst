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
#. Python、pip、Djangoの準備::

各人でpython、pip、Djangoでアプリケーションを公開できる環境を作って下さい。

続いて、django-admin startprojectを終わらせておいてください。

#. インストールする::

    pip install -U https://github.com/wiredforest/gyazowinpsvr/archive/master.tar.gz


#. settings.pyに修正を加えてきます。::

    INSTALLED_APPS = [
        ...
        'gyazosvr',  # add
        'django.contrib.sites',
        'django.contrib.sitemaps',
    ]

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    GYAZOWINPSVR_HOST = 'domain.to.gyazowinpsvr'  # must change

#. ルートのurls.pyに足す::

	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
        path('', include(gyazo_urls)),  # add
	]

#. python manage.py migrate　でモデルを追加する.

#. python manage.py runserver 等で動かし、クライアント側の設定を施した上で、アップロードする。

#. MEDIA_ROOT/up/配下にファイルが保存されていれば動作しています。
