from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenresSerializers
from .models import Genre


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all().order_by('-id')
    serializer_class = GenresSerializers


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenresSerializers
