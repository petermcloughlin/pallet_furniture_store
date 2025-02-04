from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import CustomerOrderLineItem

@receiver(post_save, sender=CustomerOrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=CustomerOrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()