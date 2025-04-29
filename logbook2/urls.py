from django.urls import path
from . import views

urlpatterns = [
   # path('api/new_user/', views.create_user, name='create_user'),
   # register
    path('api/new_user/pilot_sub/', views.create_pilot, name='create_pilot'),
    path('api/new_user/checker_sub/', views.create_checker, name='create_checker'),


    path('api/login/pilot/',views.login_p , name='Pilot Login' ), 
    path('api/login/checker/',views.login_C , name='Checker Login' ),  #........



    path('api/new_user/today_data/FlightLog/<int:user_id>/', views.post_flight_log_for_user, name='create_flight_log_for_user'),
  
    path('api/checker/today_data/get_data/', views.get_flight_log, name='getDataForChecker'),

    path('api/checker/filter/', views.filter_flight_logs, name='filter_flight_logs'),  #....

    path('api/checker/apply_marked/<int:mission_id>' , views.apply_read,  name='apply_Read'),
    path('api/checker/get_marked/' , views.get_marked,  name='Show Marked Tasks'),


]
