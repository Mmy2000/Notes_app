from django.urls import path , include , re_path as url

from . import views
app_name = 'notes_app'

urlpatterns = [
    path('' , views.notelist , name='post_list'),
    path('<int:id>/' , views.post_details , name='post_detail'),
    path('tags/<str:slug>' , views.PostByTags.as_view() , name='post_by_tags'),
    path('add/' ,views.note_add , name='add_note'),
    path('<int:id>/edit' , views.edit,name='note_edit'),
    path('<int:id>/delete' , views.delete_note,name='delete_note'),
]
