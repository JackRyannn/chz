"""chz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django import views
import myapp.views as mv
from django.conf import settings
from DjangoUeditor import urls as djud_urls
import myapp.urls as blog_url
import chz.settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mv.index),
    url(r'^ueditor/', include(djud_urls)),
    url(r'^myapp/', include(blog_url)),
    url(r'^static/(?P<path>.*)$', views.static.serve,{'document_root': chz.settings.STATIC_ROOT }),

]
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

