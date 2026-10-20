import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

# Auto-boot provisioner: Guarantees database migrations and superuser exist on any cloud container start
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
    import seed_data
    seed_data.run_seed()
    print("✓ WSGI startup: Database migrated and superuser verified successfully.")
except Exception as e:
    print("WSGI startup note:", e)


