from django.conf.urls import url

from cafe.views import CafeleListView

urlpatterns = [
    url(r'^home/$', CafeleListView.as_view(), name='home'),

]
