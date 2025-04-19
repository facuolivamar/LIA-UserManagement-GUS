"""
URL configuration for UserManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

    path('admin/', admin.site.urls),

    # API v1
    path('api/PoC/', include('core.PoC.urls')),
    path('api/PoC/schema/', SpectacularAPIView.as_view(api_version='PoC'), name='schema-PoC'),
    path('api/PoC/docs/', SpectacularSwaggerView.as_view(url_name='schema-PoC'), name='swagger-PoC'),
    path('api/PoC/redoc/', SpectacularRedocView.as_view(url_name='schema-PoC'), name='redoc-PoC'),

]