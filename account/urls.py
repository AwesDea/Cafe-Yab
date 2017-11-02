from django.conf.urls import url

from account.views import welcomeView, LoginView, signup, activate, account_activation_sent, account_activation_invalid, \
    LogoutView, profileView

urlpatterns = [
    url(r'^$', welcomeView, name='welcome'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^account_activation_invalid/$', account_activation_invalid, name='account_activation_invalid'),
    url(r'^profile/(?P<user_id>\d+)/$', profileView, name='profileView'),

]
