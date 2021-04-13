from django.db import models
from django.db.models.deletion import CASCADE

from authapp.models import User
from mainapp.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина пользователя: {self.user.username} | Товар: {self.product.name}"

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        user_products = Basket.objects.filter(user=self.user)
        return sum(
            user_product.quantity for user_product in user_products)

    def total_sum(self):
        user_products = Basket.objects.filter(user=self.user)
        return sum(user_product.sum() for user_product in user_products)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()
