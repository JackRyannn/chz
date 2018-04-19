from django.db import models

# Create your models here.

class Poem(models.Model):

    poet = models.CharField(max_length=32,default="Null")
    text = models.TextField(null=True)
    def __str__(self):
        return self.text
