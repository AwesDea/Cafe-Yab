from idlelib import autocomplete

from django.conf.urls import url

from cafe.views import CafeleListView, cafeView, searchInCafes, autocomplete, cafeRegister

urlpatterns = [
    url(r'^home/$', CafeleListView.as_view(), name='home'),
    url(r'^search/$', searchInCafes, name='search'),
    url(r'^register/$', cafeRegister, name='register'),
    url(r'^cafe/(?P<cafe_id>\d+)/$', cafeView, name='cafeView'),
    url(r'^api/autocomplete/', autocomplete, name='autocomplete'),
]
