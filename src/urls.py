"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings

from django.views.generic.base import RedirectView

from mainapp.views import *

from .api import router


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,  {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^api/groups/(?P<pk>\d+)/$', GroupsView.as_view()),
    url(r'^api/elements/(?P<pk>\d+)/$', ElementsView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^$', RedirectView.as_view(url='/api/', permanent=False))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
