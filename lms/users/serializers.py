from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "role"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data.get("email"),
            role = validated_data.get("role", 1)
        )

        user.set_password(validated_data['password'])
        user.save()

        return user