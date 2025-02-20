from rest_framework import serializers
from .models import AdRecord, AdAnalytics

class AdAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdAnalytics
        fields = "__all__"

class AdRecordSerializer(serializers.ModelSerializer):
    ad_analytics = AdAnalyticsSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = AdRecord
        fields = "__all__"  # This will now include 'ad_analytics' as a nested field
