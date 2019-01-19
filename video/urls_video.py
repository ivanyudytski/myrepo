from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^video/all', views.showall),
    re_path(r'get/(?P<video_id>\d+)/$', views.showone),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', views.addcom),
    re_path(r'^addlike/ajax/$', views.addlike)
]
