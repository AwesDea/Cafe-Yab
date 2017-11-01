from django.conf.urls import url

from account.views import welcomeView, LoginView, signup,activate,account_activation_sent,account_activation_invalid

urlpatterns = [
    url(r'^$', welcomeView, name='welcome'),
    # url(r'^home/$', LoginView.as_view(), name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^account_activation_invalid/$', account_activation_invalid, name='account_activation_invalid'),

]
