from django.conf.urls import url
from . import views
from .views import PostListView, DraftListView, MonthArchive

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='my_post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/search/$', views.post_search, name='post_search'),
    url(r'^post/draft/$', DraftListView.as_view(), name='my_draft_list'),
    url(r'^post/comments/$', views.my_comments_list, name='my_comment_list'),
    url(r'^post/draft/(?P<pk>[0-9]+)/$', views.draft_detail, name='draft_detail'),
    url(r'^post/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$', MonthArchive.as_view(), name='month_archive'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/unpublish/$', views.post_unpublish, name='post_unpublish'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]