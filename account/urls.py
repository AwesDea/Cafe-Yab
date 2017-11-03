from django.conf.urls import url

from account.views import welcomeView, LoginView, signup, account_activation_sent, account_activation_invalid, \
    LogoutView, profileView, editProfile

urlpatterns = [
    url(r'^$', welcomeView, name='welcome'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^account_activation_invalid/$', account_activation_invalid, name='account_activation_invalid'),
    url(r'^profile/(?P<user_id>\d+)/$', profileView, name='profileView'),
    url(r'^editprofile/$', editProfile, name='editprofile'),

]
