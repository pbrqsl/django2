from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer, Basket


@receiver(post_save, sender=Customer)
def create_basket(sender, instance, created, **kwargs):
    if created:
        basket = Basket.objects.create()
        id = basket.id
        customer_id = instance.id
        Customer.objects.filter(pk=customer_id).update(basket=id)


# @receiver(post_save, sender=Basket)
# def update_customer_basket(sender, instance, created, **kwargs):
#     print(instance.objects.)