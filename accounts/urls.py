from django.urls import path
from . import views 


app_name = 'accounts'

urlpatterns = [
    path('', views.home ,name = 'home'),
    path('signup' , views.signup , name='signup'),
    path('profile/' , views.profile , name='profile'),
    path('profile/edit' , views.edit_profile , name='edit_profile'),
    path('newsletter/' , views.news_letters_subscribe , name = 'newsletter'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
]