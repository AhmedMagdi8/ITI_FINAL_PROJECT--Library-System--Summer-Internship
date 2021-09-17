from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout', views.logout, name='logout')
]