from django.contrib import admin
from .models import ClientLead, ClientReview, SystemMetric, ContractBooking, ContractMessage

class ContractMessageInline(admin.TabularInline):
    model = ContractMessage
    extra = 1

@admin.register(ContractBooking)
class ContractBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'service_title', 'budget_tier', 'status', 'created_at')
    list_filter = ('status', 'budget_tier', 'created_at')
    search_fields = ('client_name', 'client_email', 'client_phone', 'project_scope')
    inlines = [ContractMessageInline]

@admin.register(ContractMessage)
class ContractMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'sender_name', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'created_at')
    search_fields = ('sender_name', 'message')

@admin.register(ClientLead)
class ClientLeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_requested', 'status', 'created_at')
    list_filter = ('status', 'service_requested')
    search_fields = ('name', 'email', 'message')

@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'rating')
    search_fields = ('client_name', 'company', 'review_text')

@admin.register(SystemMetric)
class SystemMetricAdmin(admin.ModelAdmin):
    list_display = ('metric_name', 'metric_value', 'status_label', 'updated_at')

