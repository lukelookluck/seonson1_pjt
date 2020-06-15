from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        # read_only_fields = ('db_id',)

    
class MovieSerializer(serializers.ModelSerializer):
    genre_ids = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('like',)

    
    # def create(self, validated_data):
    #     # print("asdasndkjasndkjasndkj",validated_data.get('genre_ids'))    
    #     # self.genres = validated_data.get('genre_ids')
    #     return Genre(*validated_data)

    # def update(self, instance, validated_data):
    #     print("asdasndkjasndkjasndkj",validated_data.get('like'))
    #     instance['like'] = (validated_data.get('like'))
    #     print(instance)
    #     # instance.save()
    #     return instance


class MovieLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id',)
        read_only_fields = ('like',)