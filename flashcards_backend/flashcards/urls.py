from django.urls import path
from . import views

urlpatterns = [
    path('flashcard/', views.FlashcardList.as_view()),
    path('collection/', views.CollectionList.as_view())
]