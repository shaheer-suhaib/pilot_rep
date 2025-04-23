
from django.contrib import admin 
from django.urls import path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('log_data/', include('logbook.urls'))
]
