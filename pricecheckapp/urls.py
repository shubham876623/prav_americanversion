from pricecheckapp import views
from django.urls import path

urlpatterns = [
    path('api/products/' ,views.ProductsAPIView.as_view())
]
