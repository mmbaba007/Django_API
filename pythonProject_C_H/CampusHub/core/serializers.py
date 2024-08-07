from rest_framework import serializers
from .models import Item, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'names', 'representing_image']


class SignUpSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data['email'],)
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={"input_style": "password"}, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError('Invalid Username or Password')

        attrs['user'] = user
        return attrs
