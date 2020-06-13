from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #     return User(**validated_data)

    def update(self, instance, validated_data):
        print(validated_data.get('like_movie'))
        instance.like_movie.append(validated_data.get('like_movie'))
        instance.save()
        return instance