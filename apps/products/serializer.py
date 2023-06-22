from rest_framework.serializers import ModelSerializer

from products.models import Category, ProductImage, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    images = ProductImageModelSerializer(many=True, read_only=True)
