"""django_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from website import views
from website import cmd2html

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^translate', views.translate, name='translate'),
    url(r'^info$', views.info, name='info'),
    url(r'^explain_cmd$', cmd2html.explain_cmd, name='explain_cmd'),

    url(r'^remember_ip_address$', views.remember_ip_address,
        name='remember_ip_address'),
    url(r'^recently_asked$', views.recently_asked, name='recently_asked'),

    url(r'^admin/', admin.site.urls)
]
