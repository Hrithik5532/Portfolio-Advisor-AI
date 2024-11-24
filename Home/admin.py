from django.contrib import admin
from .models import User, TargetPlan
# Register your models here.

admin.site.register(User)


@admin.register(TargetPlan)
class TargetPlanAdmin(admin.ModelAdmin):
    list_display = ('investment_type', 'investment_amount', 'risk_tolerance', 'financial_goals', 'timeline', 'created_at')
    list_filter = ('investment_type', 'risk_tolerance', 'financial_goals', 'timeline')
