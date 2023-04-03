from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sensor, SensorLog


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        temp = Sensor.objects.get(name="temperature")
        fric = Sensor.objects.get(name="friction")
        power = Sensor.objects.get(name="power")
        data = {
            'temp': temp.value,
            'fric': fric.value,
            'power': power.value
        }
        return render(request, 'index.html', data)


class TempData(APIView):
    def get(self, request, format=None):
        temp_log = reversed(SensorLog.objects.filter(name__name__exact="temperature").order_by('-id')[:10])
        time_data = []
        temp_data = []
        chart_label = "Temperature Data"
        for log in temp_log:
            time_data.append(log.time.strftime("%x %X"))
            temp_data.append(log.value)
        data = {
            "time_data": time_data,
            "chart_data": temp_data,
            "chart_label": chart_label
        }
        return Response(data)


class FricData(APIView):
    def get(self, request, format=None):
        fric_log = reversed(SensorLog.objects.filter(name__name__exact="friction").order_by('-id')[:10])
        time_data = []
        fric_data = []
        chart_label = "Friction Data"
        for log in fric_log:
            time_data.append(log.time.strftime("%x %X"))
            fric_data.append(log.value)
        data = {
            "time_data": time_data,
            "chart_data": fric_data,
            "chart_label": chart_label
        }
        return Response(data)


class PowerData(APIView):
    def get(self, request, format=None):
        power_log = reversed(SensorLog.objects.filter(name__name__exact="power").order_by('-id')[:10])
        time_data = []
        power_data = []
        chart_label = "Power Data"
        for log in power_log:
            time_data.append(log.time.strftime("%x %X"))
            power_data.append(log.value)
        data = {
            "time_data": time_data,
            "chart_data": power_data,
            "chart_label": chart_label
        }
        return Response(data)
