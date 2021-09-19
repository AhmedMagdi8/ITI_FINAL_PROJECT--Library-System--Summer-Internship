from . import views
from django.urls import path

# Main page is login page
urlpatterns = [
    path('dashboard',views.Dashboard,name='dashboard'),
    path('showborrowed/',views.showborrowedstd,name='showborrowedstd'),
    path('edit/',views.UserEditView.as_view(),name='EditProfile'),
    path('booknow/<int:book_id>/<int:user_id>',views.booknow,name='booknow'),
    path('return/<int:book_id>/<int:user_id>',views.return_book,name='return_book'),
    path('mybooks/<int:user_id>',views.mybooks,name='mybooks'),
]