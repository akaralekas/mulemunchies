from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^add/$', views.add, name='add'),
	url(r'^remove/$', views.remove, name='remove'),
	url(r'^show/$', views.show, name='show'),
	url(r'^menu/$', views.menu, name='menu'),
]