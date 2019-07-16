from django.db import models
# Create your models here.


class User(models.Model):

    username=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "曼曼"
        verbose_name_plural = "曼曼"