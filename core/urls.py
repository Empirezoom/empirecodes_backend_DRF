from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.management import call_command

def root_health_view(request):
    return JsonResponse({
        'status': 'ONLINE',
        'system': 'EmpireCodes Enterprise Microservices Hub',
        'architect': 'Anthony Oluwaseun Matthew',
        'api_root': '/api/',
        'admin_panel': '/admin/',
        'telemetry_endpoint': '/api/dashboard/',
    })

def setup_superuser_view(request):
    """
    Live web container superuser provisioner.
    Executes in the active runtime so it works across all free and paid clouds.
    """
    secret = request.GET.get('key', '')
    if secret != 'empire123224':
        return JsonResponse({'error': 'Unauthorized. Pass ?key=empire123224'}, status=403)

    # 1. Ensure migrations are applied in the live database
    try:
        call_command('migrate', interactive=False)
    except Exception as e:
        print("Migration error:", e)

    # 2. Create or reset the superuser
    User = get_user_model()
    username = request.GET.get('username', 'anthony')
    password = request.GET.get('password', 'EmpireCodes2026!')
    email = request.GET.get('email', 'matthew123224@gmail.com')

    user, created = User.objects.get_or_create(username=username)
    user.email = email
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()

    # 3. Seed initial metrics, leads and contract booking
    try:
        import seed_data
        seed_data.run_seed()
    except Exception as e:
        print("Seed error:", e)

    return JsonResponse({
        'status': 'SUCCESS',
        'message': f"Superuser '{username}' successfully provisioned in the live running database!",
        'credentials': {
            'username': username,
            'password': password,
            'admin_login_url': '/admin/',
        }
    })

urlpatterns = [
    path('', root_health_view, name='root-health'),
    path('api/setup-superuser/', setup_superuser_view, name='setup-superuser'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]



