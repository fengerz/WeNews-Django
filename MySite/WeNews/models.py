from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length = 32)

    def __str__(self):
        return self.title