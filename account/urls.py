from django.conf.urls import url

from account.views import homeview

urlpatterns = [
    url(r'^welcome/$', homeview, name='welcome'),
    url(r'^home/$', homeview, name='home'),

]
