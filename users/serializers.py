from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели  User"""
    password = serializers.CharField(min_length=8, write_only=True)
    telegram_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            telegram_id=validated_data['telegram_id']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'telegram_id')
