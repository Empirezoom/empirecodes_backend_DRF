import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import ClientLead, ClientReview, SystemMetric

def run_seed():
    print("Seeding EmpireCodes Backend Data...")

    # Seed System Metrics
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
    print("✓ Client Reviews seeded (including 1 pending approval to test mobile moderation!).")
    print("\nAll done! Run `python manage.py runserver 0.0.0.0:8000` to serve the API.")

if __name__ == '__main__':
    run_seed()

