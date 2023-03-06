from django.db import models
from base.models import BaseModel

# Create your models here.

class Category(BaseModel):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    cat_img = models.ImageField(upload_to="categories")

class Product(BaseModel):
    prod_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    prod_descp = models.TextField()

class ProdImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")