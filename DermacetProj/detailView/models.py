from django.db import models

# Create your models here.

class Contact(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Career(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cv = models.FileField(upload_to="cv")

    def __str__(self):
        return self.name
