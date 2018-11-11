"""users"""

from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    # login
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # logout
    url(r'^logout/', logout, name='logout'),
    # register
    url(r'^register$', views.register, name='register')
]
