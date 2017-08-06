


from django.conf.urls import url

from . import views


app_name = 'students'



urlpatterns = [
    url(r'^$', views.index, name='index'),

    # ex: /students/5/
    #url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),

    # added the word 'specifics'
    #url(r'^specifics/(?P<student_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),   





    # ex: /students/5/results/
    url(r'^(?P<student_id>[0-9]+)/results/$', views.results, name='results'),


]
