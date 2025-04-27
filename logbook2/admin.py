from django.contrib import admin
from .models import User, Pilot, Checker, Aircraft, FlightCategory, FlightLog

admin.site.register(User)
admin.site.register(Pilot)
admin.site.register(Checker)
admin.site.register(Aircraft)
admin.site.register(FlightCategory)
admin.site.register(FlightLog)
