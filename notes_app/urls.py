from django.urls import path , include , re_path as url

from . import views
urlpatterns = [
    path(r'^$' ,views.all_notes , name='all_notes'),
    url(r'^(%p<id>/d+)$' , views.detail,name='note_detail'),
]
