from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_post_list, name="my_post_list" )
]