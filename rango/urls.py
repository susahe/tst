from django.conf.urls import url

from . import views

urlpatterns = [ 
	url (r'^$', views.index,  name=  'index'), 
#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
  #  url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
  #  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
  
      url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
      url(r'^add_page/$', views.add_page, name='add_category'), # NEW MAPPING!

   # url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),  # New!
	
	]
