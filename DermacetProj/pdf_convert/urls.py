from django.urls import path, include  
from . import views 

# Paths

urlpatterns = [
    path('<order_id>',views.download_invoice, name="download_invoice"),
]