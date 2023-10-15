from django.db import models

# Create your models here.

class Author (models.Model):
    name= models.CharField(max_length=200)
    degree = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'authors'


class Article (models.Model):
    title = models.CharField(max_length=300)
    abstract = models.TextField()
    rank = models.IntegerField(default=1)
    is_published = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f'{self.title}/Is Published:{self.is_published}'

    class Meta:
        db_table = 'articles'




