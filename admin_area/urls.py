from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls')),
    path('teams/', include('core.urls')),
    path('', include('core.urls')),  # fallback for homepage
]
