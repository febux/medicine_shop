from django.db import models


class Staff(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    age = models.IntegerField()
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.first_name} - {self.position}"
