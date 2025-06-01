from django.contrib import admin
from django.urls import path, include
import patients.urls

urlpatterns = [
    path('api/', include('patients.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
