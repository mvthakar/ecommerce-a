from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(max_length=255)
    password_hash = models.TextField()
    role = models.ForeignKey(
        to=Role, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.email
