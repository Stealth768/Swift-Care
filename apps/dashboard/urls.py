from django.urls import path
from .views import doctor_panel, doctor_profile, consultation_page, sos_monitor

urlpatterns = [
    path('', doctor_panel, name='dashboard'),
]

# Root-level URLs for new pages
app_name = 'dashboard'

# Add these to core/urls.py instead
