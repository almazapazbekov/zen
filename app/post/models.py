from django.db import models
from django.db.models import Avg

from account.models import Author


class TextAuthorAbstract(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[0:30]}... - {self.author}'

    class Meta:
        abstract = True


class Posts(TextAuthorAbstract):

    @property
    def average_rating(self):
        #     # post=self фильтр по определенному посту
        ratings = Status.objects.filter(post=self)
        total = 0
        for rating in ratings:
            total += rating.rating
        if len(ratings) == 0:
            return 0
        else:
            return total / len(ratings)


class Comments(TextAuthorAbstract):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Status(models.Model):
    choices = [
        (None, 'None'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=choices, default=None, null=True, blank=True)


    class Meta:
        unique_together = ['post', 'author', ]

    def __str__(self):
        return f'{str(self.rating)} - {self.post}'
