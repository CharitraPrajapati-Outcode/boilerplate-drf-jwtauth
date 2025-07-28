"""
v1 API url for swagger view
"""
from django.urls import include, path

app_name = 'v1-apis'

urlpatterns = [
    path('users/', include('apps.user.api.v1.urls')),
]
