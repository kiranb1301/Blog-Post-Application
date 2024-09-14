from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup_view,name='user-signup'),
    path('login/',login_view,name='user-login'),
    path('logout/',logout1,name='user-logout'),
    path('profile/',profile_view,name='user-profile'),
]
