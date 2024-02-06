from django.urls import path
from .views import (
    ExerciseCreateListView,
    ExerciseRetrieveUpdateDestroyView
)

urlpatterns = [
    path('exercise/', ExerciseCreateListView.as_view(),
         name='exercise_list_create'),

    path('exercise/<int:pk>/', ExerciseRetrieveUpdateDestroyView.as_view(),
         name='exercise_retrieve_update_destroy')
]
