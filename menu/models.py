from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    composition = models.TextField()
    preparation_time = models.TimeField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
