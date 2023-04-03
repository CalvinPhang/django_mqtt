from django.contrib import admin

from .models import Sensor, SensorLog

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value")
    
@admin.register(SensorLog)
class SensorLogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "value", "time")

# Register your models here.
