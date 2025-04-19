from rest_framework import serializers
from ..models import (
    CustomUser,
    Subscription
)
from django.contrib.auth.models import Group, Permission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'start_date', 'end_date', 'status', 'credits_consumed', 'credits_consumed_detail', 'user']
        read_only_fields = ['id']


class CustomUserSerializer(serializers.ModelSerializer):
    # subscription = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 
            'is_staff', 'is_active', 'is_superuser',
            # 'subscription'
        ]
    
    # def get_subscription(self, obj):
    #     subscription = Subscription.objects.filter(user=obj, status='active').first()
    #     if not subscription:
    #         return None
    #     return SubscriptionSerializer(subscription).data



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        user_data = CustomUserSerializer(user).data
        for key, value in user_data.items():
            token[key] = value

        return token
