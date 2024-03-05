from django.urls import path

from movies import views

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(),
         name='movies-list-create'),

    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(),
         name='movies-detail'),
]
