"""py_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.front_page, name='front page'),
    url(r'^post/(?P<post_id>[\w]+)/$', views.detail_view, name='detail_view'),
    url(r'^bio/', views.about_view, name='about_view'),
    url(r'^cat/(?P<cat>[\w]+)/$', views.cat_view, name='cat_view')
]
