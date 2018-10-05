"""serapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view
from apps.api import views as api_views
from apps.series import views as series_views

schema_view = get_schema_view(title='Serapp API')

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

router.register(r'genres', series_views.GenreViewSet)
router.register(r'series', series_views.SerieViewSet)

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^soap/$', series_views.soap_request),

]
