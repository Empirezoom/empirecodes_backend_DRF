from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('service_requested', models.CharField(default='Full-Stack Python & DRF', max_length=120)),
                ('budget_range', models.CharField(blank=True, default='Flexible', max_length=80)),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('new', 'New Lead'), ('contacted', 'Contacted / In Discussion'), ('in_progress', 'Project In Progress'), ('closed', 'Completed / Closed'), ('archived', 'Archived')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('project_name', models.CharField(blank=True, max_length=150)),
                ('rating', models.IntegerField(default=5)),
                ('review_text', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('source', models.CharField(default='EmpireCodes Web', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SystemMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(max_length=100, unique=True)),
                ('metric_value', models.CharField(max_length=100)),
                ('status_label', models.CharField(default='OPTIMAL', max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

