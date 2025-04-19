from .views import (
    CurrentUserView,
    SubscriptionViewSet,
    UserSubscriptionSetCreditsView,
)
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()

router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = router.urls + [
    path('user/me/', CurrentUserView.as_view(), name='current-user'),
    path('user-subscription/set-credits/', UserSubscriptionSetCreditsView.as_view(), name='set-user-subscription-credits'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]