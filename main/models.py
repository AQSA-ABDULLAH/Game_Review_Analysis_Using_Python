from django.db import models;

class Game(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title