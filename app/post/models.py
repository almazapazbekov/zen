from django.db import models
from django.db.models import Avg

from account.models import Author


class Posts(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    @property
    def average_rating(self):
        #     # post=self фильтр по определенному посту
        ratings = Status.objects.filter(post=self)
        total = 0
        for rating in ratings:
            total += rating.rating

        return total/len(ratings)

    def __str__(self):
        return f'{self.text[0:10]}... - {self.author}'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    choices = [
        (None, 'none'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=choices, default=None)

    def __str__(self):
        return str(self.rating)
