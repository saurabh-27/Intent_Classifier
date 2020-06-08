from django.db import models

# Create your models here.

class Intent(models.Model):

    def __str__(self):
        return self.intent_prediction

