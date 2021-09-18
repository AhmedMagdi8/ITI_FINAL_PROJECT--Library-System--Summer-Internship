from . import views
from django.urls import path

urlpatterns = [
    path('login',views.index,name='index'),
    path('handle_login/',views.handle_login,name='handle_login'),
    path('register/',views.register,name='register'),
    path('logout', views.logout, name='logout')
]