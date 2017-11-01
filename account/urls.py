from django.conf.urls import url

from account.views import welcomeView, LoginView

urlpatterns = [
    url(r'^welcome/$', welcomeView, name='welcome'),
    url(r'^$', LoginView.as_view(), name='login'),

]
