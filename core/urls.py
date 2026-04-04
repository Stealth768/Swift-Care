from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('locator/', include('apps.locator.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('academy/', include('apps.academy.urls')),
]