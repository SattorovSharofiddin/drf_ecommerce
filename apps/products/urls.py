from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import CategoryAPIView, ProductModelViewSet

routers = DefaultRouter()
routers.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('', include(routers.urls)),
    path('category', CategoryAPIView.as_view(), name='category')
]
