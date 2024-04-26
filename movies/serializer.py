from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializers
from genres.serializers import GenresSerializers
from movies.models import Movie


class MovieSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'Resumo não deve ser maior do que 500 carateres.')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializers(many=True)
    genre = GenresSerializers()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors',
                  'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None
