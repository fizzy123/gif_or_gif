from django.conf.urls import patterns, url

from gif import views 

urlpatterns = patterns('gif.views',
	url(r'^$', 'display', name='index'),
	url(r'^rankings/$', 'rankings', name='rankings'),
)
