from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=150)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(max_length=50)),
                ('service_title', models.CharField(default='Fintech & Paystack Architecture', max_length=150)),
                ('budget_tier', models.CharField(default='Production MVP', max_length=80)),
                ('timeline', models.CharField(default='Urgent MVP (1-2 Weeks)', max_length=80)),
                ('project_scope', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending Architect Review'), ('accepted', 'Contract Accepted'), ('in_progress', 'Development In Progress'), ('audit', 'ACID & Security Audit'), ('completed', 'Production Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=30)),
                ('estimated_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContractMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='api.contractbooking')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]

