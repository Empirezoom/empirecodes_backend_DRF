from django.db import models

class ClientLead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Lead'),
        ('contacted', 'Contacted / In Discussion'),
        ('in_progress', 'Project In Progress'),
        ('closed', 'Completed / Closed'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    service_requested = models.CharField(max_length=120, default='Full-Stack Python & DRF')
    budget_range = models.CharField(max_length=80, blank=True, default='Flexible')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.service_requested}) - {self.status}"


class ClientReview(models.Model):
    client_name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=100, blank=True)
    project_name = models.CharField(max_length=150, blank=True)
    rating = models.IntegerField(default=5)
    review_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    source = models.CharField(max_length=50, default='EmpireCodes Web')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.rating}★ ({'Approved' if self.is_approved else 'Pending'})"


class SystemMetric(models.Model):
    metric_name = models.CharField(max_length=100, unique=True)
    metric_value = models.CharField(max_length=100)
    status_label = models.CharField(max_length=50, default='OPTIMAL')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.metric_name}: {self.metric_value} [{self.status_label}]"


class ContractBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Architect Review'),
        ('accepted', 'Contract Accepted'),
        ('in_progress', 'Development In Progress'),
        ('audit', 'ACID & Security Audit'),
        ('completed', 'Production Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    client_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=50) # Strictly WhatsApp preferred
    service_title = models.CharField(max_length=150, default='Fintech & Paystack Architecture')
    budget_tier = models.CharField(max_length=80, default='Production MVP')
    timeline = models.CharField(max_length=80, default='Urgent MVP (1-2 Weeks)')
    project_scope = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    estimated_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Booking #{self.id} - {self.client_name} ({self.service_title}) [{self.status}]"


class ContractMessage(models.Model):
    booking = models.ForeignKey(ContractBooking, on_delete=models.CASCADE, related_name='messages')
    sender_name = models.CharField(max_length=150)
    message = models.TextField()
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"[{'Staff' if self.is_staff else 'Client'}] {self.sender_name}: {self.message[:30]}"


