from django.db import models

# Create your models here.
from django.db.models.options import Options


class Board(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название борды', unique=True)
    url = models.CharField(max_length=10, verbose_name='Адрес борды на сервере', unique=True)


class AbstractPostModel(models.Model):

    class Meta:
        Options.abstract = True

    date = models.DateField(auto_now=True, verbose_name='Дата постинга')
    text = models.TextField(verbose_name='Текстовый контент треда')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='thread_board')
    id = models.AutoField(primary_key=True)


class Thread(AbstractPostModel):
    pass


class Post(AbstractPostModel):
    pass
