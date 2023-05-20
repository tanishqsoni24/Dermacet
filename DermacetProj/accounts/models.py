from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from shop.models import Product, Coupen
from base.emails import send_account_activation_email

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    is_cv_uploaded = models.BooleanField(default=False)

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid = False, cart__user=self.user).count()

    def __str__(self) -> str:
        return self.user.username + " - " + (lambda: "Not Verified", lambda: "Verified User")[self.is_email_verified]()

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    coupen = models.ForeignKey(Coupen, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_signature = models.CharField(max_length=100, null=True, blank=True)
    payment_done_amount = models.IntegerField(default=0, null=True, blank=True)
    cart_total_amount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    def get_cart_total(self):
        cart_items = self.cart_items.all()
        total_price = []
        for cart_item in cart_items:
            if(cart_item.product.product_available_count > 0):
                total_price.append(cart_item.product.price)
        
        if self.coupen:
            self.cart_total_amount = sum(total_price) - self.coupen.discount_price
            return sum(total_price) - self.coupen.discount_price
        self.cart_total_amount = sum(total_price)
        return sum(total_price)
    
    def set_razorpay_order_id(self, razorpay_order_id):
        self.razorpay_order_id = razorpay_order_id
        self.save()

    def set_payment_done_amount(self, payment_done_amount):
        self.payment_done_amount = payment_done_amount
        self.save()
     

class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        if self.product is not None:
            return self.product.prod_name + " by " + self.cart.user.username
        return "No product by " + self.cart.user.username


@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user=instance, email_token=email_token)
            email = instance.email
            send_account_activation_email(email, email_token)
    except Exception as e:
        print(e)
