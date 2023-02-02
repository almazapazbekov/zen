from django.db import models

from account.models import Author


class Posts(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[0:10]}... - {self.author}'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


