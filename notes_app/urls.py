from django.urls import path , include , re_path as url

from . import views
app_name = 'notes_app'

urlpatterns = [
    url(r'^$' ,views.all_notes , name='all_notes'),
    #url(r'^(?P<id>\d+)$' , views.detail,name='note_detail'),
    url(r'^(?P<slug>[-\w]+)/$' , views.detail,name='note_detail'),
]
