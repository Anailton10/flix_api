from django.urls import path

from genres import views

urlpatterns = [
    path('genre/', views.genre_creat_list_view, name='genre-create-list'),
    path('genre/<int:pk>/', views.genre_detail_view, name='genre-detail-view'),
]
