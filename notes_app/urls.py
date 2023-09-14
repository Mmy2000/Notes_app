from django.urls import path , include , re_path as url

from . import views
app_name = 'notes_app'

urlpatterns = [
    path('' , views.PostList.as_view() , name='post_list'),
    path('<slug:slug>' , views.PostDetail.as_view() , name='post_detail'),
    path('add/' ,views.note_add , name='add_note'),
    path('<str:slug>/edit' , views.edit,name='note_edit'),
    path('category/<str:slug>' , views.PostByCategory.as_view() , name='post_by_category'),
]
