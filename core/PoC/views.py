from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .BaseView import BaseViewSet

from ..models import (
    CustomUser,
    Subscription
)
from .serializers import (
    CustomUserSerializer,
    SubscriptionSerializer
)

# Create your views here.

class CurrentUserView(APIView):
    """
    Retrieve the details of the currently authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # This is the currently authenticated user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class SubscriptionViewSet(BaseViewSet):
    """
    ViewSet for managing subscriptions.
    """
    model = Subscription
    serializer_class = SubscriptionSerializer
    filterset_class = None

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=SubscriptionSerializer(many=True),
        description="Retrieve a list of Subscription entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=SubscriptionSerializer,
        description="Retrieve a single Subscription entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class UserSubscriptionSetCreditsView(APIView):
    """
    Update credits consumed for the subscription of the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=SubscriptionSerializer(partial=True),
        responses=SubscriptionSerializer,
        description="Update credits consumed for the current user's subscription"
    )
    def put(self, request):
        user = request.user

        # Get the subscription for the current user
        subscription = Subscription.objects.filter(user=user, status='active').first()
        if not subscription:
            return Response({"error": "No active subscription found for this user"}, status=404)

        # Check if credits_consumed_detail is in the request data
        if 'credits_consumed_detail' not in request.data:
            return Response({"error": "credits_consumed_detail is required"}, status=400)
        
        # Update credits_consumed_detail by adding new values to existing ones
        current_credits = subscription.credits_consumed
        current_details = subscription.credits_consumed_detail or {}
        new_details = request.data.get('credits_consumed_detail', {})
        
        # Merge the dictionaries, adding values for existing keys
        for key, value in new_details.items():
            current_credits += value
            if key in current_details:
                current_details[key] += value
            else:
                current_details[key] = value
        
        # Update the subscription with the merged details
        subscription.credits_consumed = current_credits
        subscription.credits_consumed_detail = current_details
        subscription.save()
        
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
