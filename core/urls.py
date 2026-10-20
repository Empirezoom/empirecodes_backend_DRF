from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def root_health_view(request):
    return JsonResponse({
        'status': 'ONLINE',
        'system': 'EmpireCodes Enterprise Microservices Hub',
        'architect': 'Anthony Oluwaseun Matthew',
        'api_root': '/api/',
        'admin_panel': '/admin/',
        'telemetry_endpoint': '/api/dashboard/',
    })

urlpatterns = [
    path('', root_health_view, name='root-health'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


