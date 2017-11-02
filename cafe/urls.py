from django.conf.urls import url

from cafe.views import CafeleListView, cafeView, searchInCafes

urlpatterns = [
    url(r'^home/$', CafeleListView.as_view(), name='home'),
    url(r'^search/$', searchInCafes, name='search'),
    url(r'^cafe/(?P<cafe_id>\d+)/$', cafeView, name='cafeView'),
]
