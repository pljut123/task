from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.views import serve


urlpatterns = [
    url(r'^$', views.post_list.as_view(), name='post_list'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^addlike/$', views.addlike, name ='addlike'),
    url(r'^post_follow/$', views.post_follow.as_view(), name ='post_follows'),
    url(r'^follows/$', views.follows, name ='follows'),

]