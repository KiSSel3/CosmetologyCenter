from django.conf import settings
from appointments.models import AppointmentItem


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = []

        self.cart = cart    


    def add(self, appointment_item):
        appointment_item_id = str(appointment_item.id)

        if appointment_item_id not in self.cart:
            self.cart.append(appointment_item_id)

        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True


    def remove(self, appointment_item):
        appointment_item_id = str(appointment_item.id)
        if appointment_item_id in self.cart:
            self.cart.remove(appointment_item_id)

        self.save()


    def __iter__(self):
        appointment_items = AppointmentItem.objects.filter(id__in=self.cart)

        for item in appointment_items:
            yield item


    def __len__(self):
        return len(self.cart)


    def clear(self):
        self.session[settings.CART_SESSION_ID] = []
        self.session.modified = True


    def get_total_price(self):
        appointment_items = AppointmentItem.objects.filter(id__in=self.cart)

        return sum(item.service.price for item in appointment_items)
