from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify

# Create your models here.

class Category(BaseModel):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    cat_img = models.ImageField(upload_to="categories")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.cat_name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.cat_name

class Product(BaseModel):
    prod_name = models.CharField(max_length=52)
    slug = models.SlugField(unique=True, null=True, blank=True)
    prod_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    buy_count = models.IntegerField(default=0)
    product_available_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(Product, self).save(*args, **kwargs)
    
    def set_buy_count(self, quantity):
        self.buy_count += quantity
        self.save()

    def set_product_available_count(self, quantity):
        self.product_available_count -= quantity
        self.save()

    def __str__(self):
        return self.prod_name

class Product_Description(BaseModel):
    prod_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='description')
    prod_descp = models.TextField(blank=True)

class ProdImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

class Coupen(BaseModel):
    coupen_code = models.CharField(max_length=10)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=0)
    minimun_amount = models.IntegerField(default=200)

class Reviews(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_user")
    review = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now(),blank=True)

    def __str__(self):
        return self.review


class Newsletter(BaseModel):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email
