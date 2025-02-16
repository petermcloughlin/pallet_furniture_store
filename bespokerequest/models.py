from django.db import models


class BespokeRequest(models.Model):
    name = models.CharField(max_length=254)
    telephonenumber = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Bespoke request from {self.name} | ContactNumber: {self.telephonenumber} |  Email: {self.email}"
