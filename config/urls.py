"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.v1.urls')),
]

if settings.DEBUG:
    # serve media

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    from django.views.generic import RedirectView
    from .swagger import drf_yasg_swagger_view

    urlpatterns += [
        path('', RedirectView.as_view(url='/api/docs', permanent=True), name='docs-home'),
        path('api/docs', drf_yasg_swagger_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/redoc', drf_yasg_swagger_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
