from django.db import models



class Cake(models.Model):
    # id=models.ForeignKey.CharField(max_length=11)
    cake_name = models.CharField(max_length=255)
    cake_quantity = models.PositiveIntegerField(unique=False)
    cake_price = models.PositiveIntegerField(unique=False)
    cake_description = models.CharField(max_length=255)
    cake_avatar = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.cake_name}"


from django.db import models

# Create your models here.
