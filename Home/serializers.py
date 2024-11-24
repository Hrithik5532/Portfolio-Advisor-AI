
from rest_framework import serializers
from .models import User
from .models import TargetPlan


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'temp_access_token']

class TargetPlanSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    class Meta:
        model = TargetPlan
        fields = '__all__'

    def validate(self, data):
        # Ensure either SIP or Lumpsum is provided based on the investment type
        if data['investment_type'] == 'sip' and not data.get('sip_amount'):
            raise serializers.ValidationError("SIP amount is required for SIP investment.")
        if data['investment_type'] == 'lumpsum' and not data.get('lumpsum_amount'):
            raise serializers.ValidationError("Lumpsum amount is required for Lumpsum investment.")
        return data
