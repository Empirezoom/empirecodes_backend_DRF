import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from api.models import ClientLead, ClientReview, SystemMetric, ContractBooking, ContractMessage

def run_seed():
    print("Seeding EmpireCodes Backend Data & Superuser...")

    # 1. Automatically Create / Reset Django Superuser (Zero Shell Needed!)
    User = get_user_model()
    admin_user = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'anthony')
    admin_email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'matthew123224@gmail.com')
    admin_password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')


    if not User.objects.filter(username=admin_user).exists():
        User.objects.create_superuser(username=admin_user, email=admin_email, password=admin_password)
        print(f"✓ Superuser '{admin_user}' created successfully with password '{admin_password}'!")
    else:
        user = User.objects.get(username=admin_user)
        user.set_password(admin_password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"✓ Superuser '{admin_user}' verified & password updated!")

    # 2. Seed System Metrics

    metrics = [
        ('Production SLA', '99.98%', 'NOMINAL'),
        ('Live Nodes', '9 Nodes Active', 'HEALTHY'),
        ('Database Engine', 'PostgreSQL ACID', 'ONLINE'),
        ('Avg API Latency', '42ms (Lagos/AWS)', 'OPTIMAL'),
    ]
    for name, val, status in metrics:
        SystemMetric.objects.update_or_create(
            metric_name=name,
            defaults={'metric_value': val, 'status_label': status}
        )
    print("✓ Metrics seeded.")

    # Seed Sample Client Leads
    leads = [
        {
            'name': 'Chinedu Eze',
            'email': 'chinedu@fintechpulse.ng',
            'phone': '+234 803 111 2233',
            'service_requested': 'Paystack Payment Engine & Webhooks',
            'budget_range': '₦1,500,000 - ₦2,500,000',
            'message': 'We need a bulletproof Django backend to handle Paystack transaction webhooks and recurring subscriptions.',
            'status': 'new'
        },
        {
            'name': 'Sarah Alabi',
            'email': 'sarah@montreux.com',
            'phone': '+234 812 444 5566',
            'service_requested': 'E-Commerce DRF + React Decoupled',
            'budget_range': '₦3,000,000',
            'message': 'Upgrading our Montreux fashion inventory management and checkout APIs.',
            'status': 'in_progress'
        },
        {
            'name': 'David Adeleke',
            'email': 'david@brokershub.ng',
            'phone': '+234 809 777 8899',
            'service_requested': 'AWS Cloud Architecture & PostgreSQL Tuning',
            'budget_range': '₦2,000,000',
            'message': 'Need database query optimization and Redis caching layer to handle 20k daily visitors.',
            'status': 'contacted'
        }
    ]
    for lead_data in leads:
        ClientLead.objects.get_or_create(email=lead_data['email'], defaults=lead_data)
    print("✓ Client Leads seeded.")

    # Seed Reviews
    reviews = [
        {
            'client_name': 'Kenechukwu O.',
            'company': 'Montreux & Co.',
            'role': 'Product Lead',
            'project_name': 'E-Commerce Architecture',
            'rating': 5,
            'review_text': 'Anthony engineered our entire backend API. Zero double-charges, idempotent webhooks, and flawless Paystack integration.',
            'is_approved': True
        },
        {
            'client_name': 'Babajide Santos',
            'company': 'BrokersHub Nigeria',
            'role': 'Technical Director',
            'project_name': 'Portal Scaling',
            'rating': 5,
            'review_text': 'Reduced our page response latencies by 35%. Excellent mathematician and backend architect.',
            'is_approved': True
        },
        {
            'client_name': 'Dr. A. Adebayo',
            'company': 'Somolu Local Government',
            'role': 'Procurement Director',
            'project_name': 'Vendor Database Digitization',
            'rating': 5,
            'review_text': 'Anthony digitized 50+ contractor registries and introduced mathematical optimization to our budget planning.',
            'is_approved': True
        },
        {
            'client_name': 'Tunde Bakare',
            'company': 'P2PEXC Crypto',
            'role': 'Founder',
            'project_name': 'Escrow Ledger System',
            'rating': 5,
            'review_text': 'Strict ACID compliance, clean DRF endpoints, and great communicator throughout the sprint.',
            'is_approved': False # Pending approval to test mobile approve button!
        }
    ]
    for rev in reviews:
        ClientReview.objects.get_or_create(
            client_name=rev['client_name'],
            company=rev['company'],
            defaults=rev
        )
    # Seed Sample Contract Booking & In-App Chat
    booking, created = ContractBooking.objects.get_or_create(
        client_email='client@empirecodes.com.ng',
        defaults={
            'client_name': 'Kenechukwu O.',
            'client_phone': '+234 817 305 7810',
            'service_title': 'Fintech & Paystack Architecture',
            'budget_tier': 'Production MVP',
            'timeline': 'Urgent MVP (1-2 Weeks)',
            'project_scope': 'Complete payment engine overhaul with webhook signature verification and idempotent ledger transactions.',
            'status': 'in_progress',
        }
    )
    if created:
        ContractMessage.objects.create(
            booking=booking,
            sender_name='Kenechukwu O.',
            message='Hello Anthony, we have submitted our Paystack secret keys and webhook endpoints for review.',
            is_staff=False
        )
        ContractMessage.objects.create(
            booking=booking,
            sender_name='Anthony (Staff Architect)',
            message='Received! We are running HMAC-SHA512 verification tests right now and locking row-level isolation.',
            is_staff=True
        )
    print("✓ Sample Contract Booking & Live Two-Way Chat seeded.")

    print("\nAll done! Run `python manage.py runserver 0.0.0.0:8000` to serve the API.")

if __name__ == '__main__':
    run_seed()

