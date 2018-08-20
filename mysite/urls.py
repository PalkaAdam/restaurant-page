from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^karta-win/$', views.whine, name='whine'),
    url(r'^koktajle/$', views.cocktails, name='cocktails'),
    url(r'^lunch/$', views.lunch, name='lunch'),
]
