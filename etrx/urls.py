from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^laptops/(?P<laptops_id>[0-9]+)/$', views.detail, name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('contact_page/', views.contact_page, name="contact_page"),
    re_path(r'^success/(?P<success_id>[0-9]+)/$', views.success, name="success"),
    re_path(r'^contact_thanks/', views.contact_thanks, name="contact_thanks"),

]