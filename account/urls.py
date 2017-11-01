from django.conf.urls import url

from account.views import welcomeView, LoginView, signup

urlpatterns = [
    url(r'^$', welcomeView, name='welcome'),
    url(r'^home/$', LoginView.as_view(), name='home'),
    url(r'^signup/$', signup, name='signup'),

]
