from django.db import models

class Type(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class Items(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # optional image upload path

    def __str__(self):
        return self.name


#Jathavedas
#meenu
