from django.conf.urls import url

from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
    # list dirs and notes
    url(r'^notes/(?P<dir_id>\d+)?$', views.notes, name='notes'),
    ## add dir
    #url(r'^new_dir/$', views.new_dir, name='new_dir'),
    ## add note
    #url(r'^new_note/dir1/$', views.new_note, name='new_note'),
    ## modify item
    #url(r'^edit/id/$', views.edit, name='edit'),
    ## delete item
    #url(r'^delete/id/$', views.delete, name='delete'),
]
