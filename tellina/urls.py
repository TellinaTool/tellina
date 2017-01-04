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

from . import views
from . import cmd2html

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^explain_cmd/', cmd2html.explain_cmd, name='explain_cmd'),

    url(r'^websearch/', views.web_search, name='websearch'),

    url(r'^task/', views.task),
    url(r'^task1/', views.task1),
    url(r'^task2/', views.task2),
    url(r'^task3/', views.task3),
    url(r'^task4/', views.task4),

    url(r'^mockups/translate.html', views.mockup_translate)
]
