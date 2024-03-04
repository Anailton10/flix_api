from rest_framework import generics
from genres.serializers import GenresSerializers
from .models import Genre


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all().order_by('-id')
    serializer_class = GenresSerializers


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializers
