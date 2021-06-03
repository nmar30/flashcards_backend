from django.db import models


class Flashcard(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    collection = models.ForeignKey(
        'Collection',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.front


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name