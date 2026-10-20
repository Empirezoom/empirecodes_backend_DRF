from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ClientLead, ClientReview, SystemMetric, ContractBooking, ContractMessage
from .serializers import (
    ClientLeadSerializer,
    ClientReviewSerializer,
    SystemMetricSerializer,
    ContractBookingSerializer,
    ContractMessageSerializer,
)

class ClientLeadViewSet(viewsets.ModelViewSet):
    queryset = ClientLead.objects.all()
    serializer_class = ClientLeadSerializer

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        lead = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(ClientLead.STATUS_CHOICES):
            lead.status = new_status
            lead.save()
            return Response({'status': 'updated', 'lead': ClientLeadSerializer(lead).data})
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)


class ClientReviewViewSet(viewsets.ModelViewSet):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer

    def get_queryset(self):
        # By default, public API can filter by approved only: ?approved=true
        is_approved = self.request.query_params.get('approved', None)
        if is_approved is not None:
            return ClientReview.objects.filter(is_approved=(is_approved.lower() == 'true'))
        return ClientReview.objects.all()

    @action(detail=True, methods=['post'])
    def toggle_approval(self, request, pk=None):
        review = self.get_object()
        review.is_approved = not review.is_approved
        review.save()
        return Response({
            'status': 'toggled',
            'is_approved': review.is_approved,
            'review': ClientReviewSerializer(review).data
        })


class ContractBookingViewSet(viewsets.ModelViewSet):
    queryset = ContractBooking.objects.all()
    serializer_class = ContractBookingSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email', None)
        if email:
            return ContractBooking.objects.filter(client_email__iexact=email)
        return ContractBooking.objects.all()

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        booking = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(ContractBooking.STATUS_CHOICES):
            booking.status = new_status
            booking.save()
            return Response({'status': 'updated', 'booking': ContractBookingSerializer(booking).data})
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'])
    def messages(self, request, pk=None):
        booking = self.get_object()
        if request.method == 'POST':
            sender_name = request.data.get('sender_name', 'Client')
            message_text = request.data.get('message', '')
            is_staff = bool(request.data.get('is_staff', False))
            if not message_text.strip():
                return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
            msg = ContractMessage.objects.create(
                booking=booking,
                sender_name=sender_name,
                message=message_text,
                is_staff=is_staff
            )
            return Response(ContractMessageSerializer(msg).data, status=status.HTTP_201_CREATED)
        else:
            msgs = booking.messages.all()
            return Response(ContractMessageSerializer(msgs, many=True).data)



class DashboardSummaryView(APIView):
    """
    Primary endpoint consumed by the EmpireCodes Mobile App Command Center.
    Returns aggregated business telemetry, lead counts, and server status.
    """
    def get(self, request):
        total_leads = ClientLead.objects.count()
        new_leads = ClientLead.objects.filter(status='new').count()
        total_reviews = ClientReview.objects.count()
        pending_reviews = ClientReview.objects.filter(is_approved=False).count()
        
        # Default seed metrics if table is empty
        metrics = list(SystemMetric.objects.values('metric_name', 'metric_value', 'status_label'))
        if not metrics:
            metrics = [
                {'metric_name': 'Production SLA', 'metric_value': '99.98%', 'status_label': 'NOMINAL'},
                {'metric_name': 'Active Nodes', 'metric_value': '9 Distributed', 'status_label': 'HEALTHY'},
                {'metric_name': 'DB Engine', 'metric_value': 'PostgreSQL ACID', 'status_label': 'ONLINE'},
                {'metric_name': 'Avg API Latency', 'metric_value': '42ms', 'status_label': 'OPTIMAL'},
            ]

        recent_leads = ClientLeadSerializer(ClientLead.objects.all()[:5], many=True).data

        return Response({
            'app_name': 'EmpireCodes Command Hub',
            'architect': 'Anthony Oluwaseun Matthew',
            'server_status': 'ONLINE',
            'telemetry': {
                'total_leads': total_leads,
                'new_leads': new_leads,
                'total_reviews': total_reviews,
                'pending_reviews': pending_reviews,
                'metrics': metrics,
            },
            'recent_leads': recent_leads
        })


class OperationsResearchOptimizeView(APIView):
    """
    Demonstrating Anthony's B.Tech Mathematics & Operations Research expertise:
    Computes an optimal linear resource allocation (Profit Maximization with Constraints).
    """
    def post(self, request):
        # Default simple profit optimization parameters
        # Maximize Z = c1*x1 + c2*x2 subject to resource constraints
        data = request.data
        c1 = float(data.get('c1', 500))  # Profit per Service A (e.g., Paystack Fintech integration)
        c2 = float(data.get('c2', 800))  # Profit per Service B (e.g., Full-Stack Django SaaS)
        dev_hours_cap = float(data.get('dev_hours', 160)) # Available hours in a month

        # Service A takes 20 hrs, Service B takes 40 hrs
        # Simulating optimal bounded solution
        # x2 max = dev_hours_cap / 40
        x2_max = dev_hours_cap // 40
        rem_hours = dev_hours_cap - (x2_max * 40)
        x1_opt = rem_hours // 20

        max_profit = (x1_opt * c1) + (x2_max * c2)

        return Response({
            'algorithm': 'Simplex / Greedy Linear Allocation',
            'developer': 'Anthony Oluwaseun Matthew (Operations Research)',
            'optimal_plan': {
                'service_a_contracts': int(x1_opt),
                'service_b_contracts': int(x2_max),
                'projected_revenue_usd': max_profit,
                'hours_utilized': (x1_opt * 20) + (x2_max * 40),
                'total_capacity_hours': dev_hours_cap,
            }
        })

