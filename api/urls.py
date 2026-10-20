from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientLeadViewSet,
    ClientReviewViewSet,
    ContractBookingViewSet,
    DashboardSummaryView,
    OperationsResearchOptimizeView,
)

router = DefaultRouter()
router.register(r'leads', ClientLeadViewSet, basename='leads')
router.register(r'reviews', ClientReviewViewSet, basename='reviews')
router.register(r'bookings', ContractBookingViewSet, basename='bookings')

urlpatterns = [
    path('dashboard/', DashboardSummaryView.as_view(), name='dashboard-summary'),
    path('optimize/', OperationsResearchOptimizeView.as_view(), name='or-optimize'),
    path('', include(router.urls)),
]

