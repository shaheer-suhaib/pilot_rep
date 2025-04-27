from django.urls import path
from . import views

urlpatterns = [
    path('api/new_user/', views.create_user, name='create_user'),
    path('api/new_user/today_data/Aircraft/<int:user_id>/', views.post_aircraft_for_user, name='post_aircraft_for_user'),
    path('api/new_user/today_data/FlightCategory/<int:user_id>/', views.postF_category_for_user, name='create_category_for_user'),
    
    path('api/new_user/pilot_sub/', views.create_pilot, name='create_pilot'),

    path('api/new_user/checker_sub/', views.create_checker, name='create_checker'),
    path('api/new_user/today_data/FlightLog/<int:user_id>/<int:AirCraID>/<int:FlighCatID>/', views.post_flight_log_for_user, name='create_flight_log_for_user'),




]
