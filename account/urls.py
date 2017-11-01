from django.conf.urls import url

from account.views import welcomeView, LoginView, signupView

urlpatterns = [
    url(r'^$', welcomeView, name='welcome'),
    url(r'home/^$', LoginView.as_view(), name='home'),
    url(r'signup/^$', signupView, name='signup'),

]
