# social_app/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login, name="login"),
    # url('', include('social_django.urls', namespace="social")),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
    # path('/login/vk-oauth2', include('social_django.urls')),


]