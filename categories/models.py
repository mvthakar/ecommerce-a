from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  parent_category = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
