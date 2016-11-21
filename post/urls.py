from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.views import serve


urlpatterns = [
    url(r'^$', views.post_list.as_view(), name='post_list'),
    url(r'^submit$', views.submit, name='submit'),

]