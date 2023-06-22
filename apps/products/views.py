from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.filters import CustomFilter
from products.models import Category, Product, ProductImage
from products.serializer import CategoryModelSerializer, ProductModelSerializer

images_params = openapi.Parameter('images', openapi.IN_FORM, description="test manual param", type=openapi.TYPE_ARRAY,
                                  items=openapi.Items(type=openapi.TYPE_FILE), required=True)


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    parser_classes = MultiPartParser, FormParser
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CustomFilter
    search_fields = ['title', 'brand', 'description']
    ordering_fields = ['id', 'title', 'price']

    @swagger_auto_schema(manual_parameters=[images_params])
    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            images_list = []
            for image in images:
                images_list.append(ProductImage(image=image, product=product))
            ProductImage.objects.bulk_create(images_list)
        return Response(serializer.data)
