import jwt, datetime
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )
        print(user)
        if not user:
            return Response({"detail": "Invalid credentails"}, status=403)
        payload = {
            "user_id": user.id,
            "exp": datetime.datetime.now() + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
        return Response({"token": token})
    