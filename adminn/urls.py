from . import views
from django.urls import path

# Main page is login page
urlpatterns = [
    path('dashboard',views.Dashboard,name='Dashboard'),
    path('showborrowed/',views.showborrowed,name='showborrowed'),
    path('editbook/<int:book_id>',views.editbook,name='editbook'),
    path('deletebook/<int:book_id>',views.deletebook,name='deletebook'),
    path('showstudents/',views.show,name='showstudents'),
    path('student/<int:student_id>',views.showstudent,name='student'),
    path('add/',views.add,name='add'),
    path('changepass/<int:user_id>',views.changepass,name='changepass'),
]