from django.urls import path
from . import views

urlpatterns = [
    path('collection/<int:collection>', views.FlashcardList.as_view()),
    path('collection/', views.CollectionList.as_view())
]