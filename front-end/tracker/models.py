from django.db import models
from django.contrib.auth import get_user_model

class Warehouse(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuty_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name