from django.db import models


# Create your models here.
class ServiceReview(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    review = models.TextField()

    def __str__(self):
        return f"Service review from {self.name} | Email: {self.email} | Review: {self.review}"
