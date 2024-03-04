from django.urls import path

from genres import views

urlpatterns = [
    path('genre/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genre/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
