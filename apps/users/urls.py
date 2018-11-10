"""users"""

from django.conf.urls import url
from django.contrib.auth.views import login, logout

urlpatterns = [
    # login page
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    # logout page
    url(r'^logout/', logout, name='logout'),
]
