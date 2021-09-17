from . import views
from django.urls import path

# Main page is login page
urlpatterns = [
    path('',views.Dashboard,name='Dashboard'),
    path('edit/',views.UserEditView.as_view(),name='EditProfile'),
    path('showstudents/',views.show,name='showstudents'),
    path('add/',views.show,name='add'),
    path('search/',views.show,name='search'),
    path('mybooks/',views.show,name='mybooks'),
    path('changepass/',views.show,name='changepass'),
    path('',views.logout,name='Logout'),
]