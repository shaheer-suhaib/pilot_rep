from . import views
from django.urls import path

urlpatterns = [
    path('',views.getLog),
    
    path('create/',views.create),
    path('<str:pk>/update/',views.update),
    path('<str:pk>/delete/',views.delete),
    path('<str:A_type>/',views.getAirCraft),

]
