from django.urls import path
from .views import doctor_panel

urlpatterns = [
    path('', doctor_panel, name='dashboard'),
]