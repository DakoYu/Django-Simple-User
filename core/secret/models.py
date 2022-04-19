from tkinter import CASCADE
from django.db import models
from django.conf import settings

class SecretModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    secret = models.IntegerField(blank=False)

    def __str__(self): return self.secret
