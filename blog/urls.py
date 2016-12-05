from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_post_list, name="my_post_list" ),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/draft/$', views.my_draft_list, name="my_draft_list"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
]