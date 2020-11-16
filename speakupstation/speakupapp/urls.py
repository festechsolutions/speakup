from django.urls import path
from . import views
urlpatterns = [

    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('logAndSign', views.tologAndSign, name='logAndSign'),
    path('mycourse', views.myCourse, name='myCourse'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('allCourses', views.allCourses, name='allCourses'),
    path('coursePage', views.coursePage1, name="coursePage"),
    path('lesson', views.showlesson, name="lesson"),
]
