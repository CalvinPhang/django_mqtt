from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    path('api/temp', views.TempData.as_view()),
    path('api/fric', views.FricData.as_view()),
    path('api/power', views.PowerData.as_view()),
]