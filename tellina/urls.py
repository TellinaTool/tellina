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

from website import annotator, cmd2html, views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^translate$', views.translate),
    url(r'^info$', views.info),

    url(r'^remember_ip_address$', views.remember_ip_address),
    url(r'^vote$', views.vote),

    url(r'^$', annotator.login),
    url(r'^login$', annotator.login),
    url(r'^register_user', annotator.register_user),
    url(r'^user_login$', annotator.user_login),
    url(r'^logout$', annotator.user_logout),

    url(r'^url_panel$', annotator.url_panel),
    url(r'^utility_panel$', annotator.utility_panel),

    url(r'^collect_page$', annotator.collect_page),
    url(r'^previous_url$', annotator.previous_url),
    url(r'^next_url$', annotator.next_url),
    url(r'^submit_annotation$', annotator.submit_annotation),
    url(r'^submit_edit$', annotator.submit_edit),
    url(r'^delete_annotation$', annotator.delete_annotation),
    url(r'^update_progress', annotator.update_progress),

    url(r'^submit_update', annotator.submit_update),
    url(r'^get_updates', annotator.get_updates),
    url(r'^get_update_replies', annotator.get_update_replies),

    url(r'^explain_cmd$', cmd2html.explain_cmd),

    url(r'^admin', admin.site.urls)
]