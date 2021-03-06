from decimal import *

from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Namuseta(models.Model):
    name = models.CharField(max_length=100)
    mobilepay = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topup", kwargs={"user_id": self.pk})

    def account_balance(self):
        t = Transaction.objects.filter(user=self).aggregate(sum=Sum("price"))
        t_sum = t["sum"] or Decimal(0.00)
        d = Deposit.objects.filter(user=self).aggregate(sum=Sum("amount"))
        d_sum = d["sum"] or Decimal(0.00)
        balance = round(d_sum - t_sum, 2)
        return balance


class Product(models.Model):
    class Meta:
        ordering = ["name"]

    CATEGORY_OPTIONS = (
        ("z", "Freezer"),
        ("f", "Fridge"),
        ("c", "Cabinet"),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=CATEGORY_OPTIONS, default="c")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to="namukilke/products")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def inventory_level(self):
        t_sum = Transaction.objects.filter(product=self).count()
        r = Restock.objects.filter(product=self).aggregate(sum=Sum("quantity"))
        r_sum = r["sum"] or 0
        inv = r_sum - t_sum
        return inv


class Transaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")


class Deposit(models.Model):
    PAYMENT_METHOD_OPTIONS = (
        ("c", "Cash"),
        ("m", "MobilePay"),
        ("r", "Refund"),
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(
        max_length=1, choices=PAYMENT_METHOD_OPTIONS, default="c",
    )

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")


class Restock(models.Model):
    RESTOCK_TYPES = (
        ("s", "Stock"),
        ("r", "Refund"),
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    type = models.CharField(max_length=1, choices=RESTOCK_TYPES, default="s",)

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")


class Feedback(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title
