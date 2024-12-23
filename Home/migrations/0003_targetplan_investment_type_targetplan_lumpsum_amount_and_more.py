# Generated by Django 5.1.3 on 2024-11-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_targetplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='targetplan',
            name='investment_type',
            field=models.CharField(choices=[('sip', 'SIP (Systematic Investment Plan)'), ('lumpsum', 'Lumpsum Investment')], default='sip', max_length=10),
        ),
        migrations.AddField(
            model_name='targetplan',
            name='lumpsum_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Total investment amount if Lumpsum is selected', max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='targetplan',
            name='sip_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Monthly SIP amount if SIP is selected', max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='targetplan',
            name='investment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
