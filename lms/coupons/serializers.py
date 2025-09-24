from rest_framework import serializers
from .models import Coupons

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = "__all__"
        read_only_fields = ["creator", "status"]
        