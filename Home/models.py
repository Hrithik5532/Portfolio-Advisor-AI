from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime  # Import the datetime module

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    temp_access_token = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.id)
    


class TargetPlan(models.Model):
    RISK_TOLERANCE_CHOICES = [
        ('conservative', 'Conservative'),
        ('moderate', 'Moderate'),
        ('aggressive', 'Aggressive'),
    ]
    FINANCIAL_GOALS_CHOICES = [
        ('retirement', 'Retirement'),
        ('education', 'Education'),
        ('wealth_accumulation', 'Wealth Accumulation'),
    ]
    TIMELINE_CHOICES = [
        ('short_term', 'Short Term'),
        ('medium_term', 'Medium Term'),
        ('long_term', 'Long Term'),
    ]
    INVESTMENT_TYPE_CHOICES = [
        ('sip', 'SIP (Systematic Investment Plan)'),
        ('lumpsum', 'Lumpsum Investment'),
    ]
    INVESTMENT_EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    HEALTH_STATUS_CHOICES = [
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor'),
    ]
    
    # New investment type field
    investment_type = models.CharField(
        max_length=10, 
        choices=INVESTMENT_TYPE_CHOICES, 
        default='sip'
    )
    
    # SIP and Lumpsum-specific fields
    sip_amount = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True,
        help_text="Monthly SIP amount if SIP is selected"
    )
    lumpsum_amount = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True,
        help_text="Total investment amount if Lumpsum is selected"
    )
    
    # Existing fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    risk_tolerance = models.CharField(max_length=20, choices=RISK_TOLERANCE_CHOICES)
    financial_goals = models.CharField(max_length=30, choices=FINANCIAL_GOALS_CHOICES)
    timeline = models.CharField(max_length=20, choices=TIMELINE_CHOICES)
    income = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    expenses = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    savings = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    debt_levels = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    age = models.PositiveIntegerField()
    liquidity_needs = models.BooleanField(default=False)
    preferred_investments = models.JSONField(default=list, blank=True)
    geographical_preferences = models.CharField(max_length=100, null=True, blank=True)
    tax_considerations = models.BooleanField(default=False)
    current_investments = models.JSONField(default=dict, blank=True)
    investment_experience = models.CharField(max_length=20, choices=INVESTMENT_EXPERIENCE_CHOICES)
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES, null=True, blank=True)
    expected_returns = models.CharField(max_length=50, null=True, blank=True)
    esg_preferences = models.BooleanField(default=False)
    dependents = models.PositiveIntegerField(default=0)
    emergency_fund_status = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    planned_contributions = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    # Auto-calculated investment amount based on SIP or Lumpsum
    investment_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Calculate investment amount based on type
        if self.investment_type == 'sip' and self.sip_amount:
            self.investment_amount = self.sip_amount * 12  # Annualize the SIP
        elif self.investment_type == 'lumpsum' and self.lumpsum_amount:
            self.investment_amount = self.lumpsum_amount
        else:
            self.investment_amount = None
        super().save(*args, **kwargs)
