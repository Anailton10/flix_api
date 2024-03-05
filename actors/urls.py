from django.urls import path

from actors import views

urlpatterns = [
    path('actors/',
         views.ActorListCreateView.as_view(), name='actor-list-create'),

    path('actors/<int:pk>/',
         views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-datail'),
]
