from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=255)
  parent_category = models.ForeignKey("self", null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
