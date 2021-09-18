from . import views
from django.urls import path

# Main page is login page
urlpatterns = [
    path('',views.Dashboard,name='Dashboard'),
    path('showborrowed/',views.showborrowed,name='showborrowed'),
    path('edit/',views.UserEditView.as_view(),name='EditProfile'),
    path('editbook/<int:book_id>',views.editbook,name='editbook'),
    path('deletebook/<int:book_id>',views.deletebook,name='deletebook'),
    path('showstudents/',views.show,name='showstudents'),
    path('student/<int:student_id>',views.showstudent,name='student'),
    path('add/',views.add,name='add'),
    path('mybooks/',views.show,name='mybooks'),
    path('changepass/<int:user_id>',views.changepass,name='changepass'),
]