from django.apps import AppConfig


class ShippingConfig(AppConfig):
    name = 'shipping'
    def ready(self):
        import shipping.signals

