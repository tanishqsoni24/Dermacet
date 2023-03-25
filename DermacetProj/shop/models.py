from django.db import models
from base.models import BaseModel
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
    prod_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    prod_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    prod_descp = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.prod_name)
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.prod_name

class ProdImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")