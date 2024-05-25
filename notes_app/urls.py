from django.urls import path , include , re_path as url

from . import views
from . import api_views

app_name = 'notes_app'

urlpatterns = [
    path('' , views.notelist , name='post_list'),
    path('id=<int:id>/' , views.post_details , name='post_detail'),
    path('tags/<str:slug>' , views.PostByTags.as_view() , name='post_by_tags'),
    path('add/' ,views.note_add , name='add_note'),
    path('<int:id>/edit' , views.edit,name='note_edit'),
    path('<int:id>/delete' , views.delete_note,name='delete_note'),
    ## api urls ##
    # path('api/list' , api_views.NotesListApi.as_view(), name='notes_api_list'),
    path('api/list' , api_views.post_list, name='notes_api_list'),
    path('api/list/<int:id>' , api_views.post_deatils_api, name='notes_api_details'),
    # path('api/list/<int:pk>' , api_views.NotesDetailsApi.as_view(), name='notes_api_detail')
    
]
