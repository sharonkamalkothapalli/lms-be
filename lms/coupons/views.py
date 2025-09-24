from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Coupons
from .serializers import CouponSerializer
from authapi.permissions import JWTAuthentication


class CouponsViewSet(viewsets.ModelViewSet):
    queryset = Coupons.objects.all()
    serializer_class = CouponSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 3:
            return Response({"detail": "Not all to create coupon"}, status=403)
        serializer.save(creator=self.request.user) 

    def update(self, request, *args, **kwargs):
        coupon = self.get_object()
        if coupon.creator != self.request.user:
            return Response({"detail": "Not allowed"}, status=403)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        coupon = self.get_object()
        if coupon.creator != self.request.user:
            return Response({"detail": "Not allowed"}, status=403)
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=True, methods=['POST'])
    def approve(self, request, pk=None):
        coupon = self.get_object()
        if request.user.role !=2:
            return Response({"detail": "Not allowed"}, status=403)
        coupon.status = "approved"
        coupon.save()
        return Response(CouponSerializer(coupon).data)
    
    @action(detail=True, methods=['POST'])
    def deny(self, request, pk=None):
        coupon = self.get_object()
        if coupon.creator != 2:
            return Response({"detail": "Not allowed"}, status=403)
        coupon.status = "denied"
        coupon.save()
        return Response(CouponSerializer(coupon).data)
    
    
