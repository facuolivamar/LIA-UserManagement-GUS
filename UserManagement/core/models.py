from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    # Add any additional fields you want here
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.

class Subscription(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    ESTADO_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(
        max_length=8,
        choices=ESTADO_CHOICES,
        default='active'
    )

    credits_consumed = models.IntegerField(default=0)
    credits_consumed_detail = models.JSONField(default=dict)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )

    def __str__(self):
        return f"Subscription {self.id} for {self.user.username}"
