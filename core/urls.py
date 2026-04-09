from django.contrib import admin
from django.urls import path, include
from apps.dashboard.views import doctor_profile, consultation_page, sos_monitor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('locator/', include('apps.locator.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('academy/', include('apps.academy.urls')),
    path('doctor-profile/', doctor_profile, name='doctor_profile'),
    path('consultation/', consultation_page, name='consultation'),
    path('sos-monitor/', sos_monitor, name='sos_monitor'),
]