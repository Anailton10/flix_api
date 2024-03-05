from rest_framework import serializers

from movies.models import Movie


class MovieSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
