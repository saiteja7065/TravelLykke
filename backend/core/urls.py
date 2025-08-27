from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('travel-options/', views.travel_options, name='travel_options'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('add-travel-option/', views.add_travel_option, name='add_travel_option'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('profile/', views.profile, name='profile'),
]
