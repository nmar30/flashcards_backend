from django.shortcuts import render
from .models import Flashcard, Collection
from .serializers import FlashcardSerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FlashcardList(APIView):
    def get_object(self, collection):
        try:
            return Flashcard.objects.filter(collection=collection)
        except Flashcard.DoesNotExist:
            raise Http404

    def get(self, request, collection):
        flashcard = self.get_object(collection)
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionList(APIView):
    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)