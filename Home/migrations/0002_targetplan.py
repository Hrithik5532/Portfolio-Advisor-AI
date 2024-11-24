# Generated by Django 5.1.3 on 2024-11-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('risk_tolerance', models.CharField(choices=[('conservative', 'Conservative'), ('moderate', 'Moderate'), ('aggressive', 'Aggressive')], max_length=20)),
                ('financial_goals', models.CharField(choices=[('retirement', 'Retirement'), ('education', 'Education'), ('wealth_accumulation', 'Wealth Accumulation')], max_length=30)),
                ('timeline', models.CharField(choices=[('short_term', 'Short Term'), ('medium_term', 'Medium Term'), ('long_term', 'Long Term')], max_length=20)),
                ('income', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('expenses', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('savings', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('debt_levels', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('age', models.PositiveIntegerField()),
                ('liquidity_needs', models.BooleanField(default=False)),
                ('preferred_investments', models.JSONField(blank=True, default=list)),
                ('geographical_preferences', models.CharField(blank=True, max_length=100, null=True)),
                ('tax_considerations', models.BooleanField(default=False)),
                ('current_investments', models.JSONField(blank=True, default=dict)),
                ('investment_experience', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=20)),
                ('health_status', models.CharField(blank=True, choices=[('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], max_length=20, null=True)),
                ('expected_returns', models.CharField(blank=True, max_length=50, null=True)),
                ('esg_preferences', models.BooleanField(default=False)),
                ('dependents', models.PositiveIntegerField(default=0)),
                ('emergency_fund_status', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('planned_contributions', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]