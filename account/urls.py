from django.conf.urls import url

from account.views import homeview, welcomeView

urlpatterns = [
    url(r'^welcome/$', welcomeView, name='welcome'),
    url(r'^home/$', homeview, name='home'),

]
