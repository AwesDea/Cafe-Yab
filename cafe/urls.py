from django.conf.urls import url

from cafe.views import CafeleListView, cafeView

urlpatterns = [
    url(r'^home/$', CafeleListView.as_view(), name='home'),
    url(r'^cafe/$', cafeView, name='cafe'),

]
