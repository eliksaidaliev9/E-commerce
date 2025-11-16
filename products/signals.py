import requests
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from products.models import Order


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        token = settings.TELEGRAM_BOT_TOKEN
        method = 'sendMessage'

        message_text = (
            f"New Order: {instance.id}\n"
            f"Product: {instance.product.name}\n"
            f"Quantity: {instance.quantity}\n"
            f"Client: {instance.customer.username}\n"
            f"Tel: {instance.phone_number}"
        )

        response = requests.post(
            url=f'https://api.telegram.org/bot{token}/{method}',
            data={
                'chat_id': 74163413,
                'text': message_text,
            }
        ).json()