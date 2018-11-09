"""work_notes"""

from django.conf.urls import url, include

from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
    # list dirs and notes
    url(r'^items/', include([
        url(r'^dir/(?:(?P<dir_id>\d+)/)?$', views.dir, name='dir'),
        url(r'note/(?P<note_id>\d+)/', views.note, name='note'),
    ], namespace='items')),
    # add dir
    url(r'^new_dir/$', views.new_dir, name='new_dir'),
    # add note
    url(r'^new_note/(?:(?P<dir_id>\d+)/)?$', views.new_note, name='new_note'),
    # edit note
    url(r'^edit_note/(?P<note_id>\d+)/$', views.edit_note, name='edit_note'),
    # edit dir
    #url(r'^edit_dir/(?P<dir_id>\d+)/&', views.edit_dir, name='edit_dir')
    ## delete item
    #url(r'^delete/id/$', views.delete, name='delete'),
]
