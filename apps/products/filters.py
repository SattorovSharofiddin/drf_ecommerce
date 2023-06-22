from django_filters import FilterSet, NumberFilter
from products.models import Product


class CustomFilter(FilterSet):
    price__to = NumberFilter(field_name='price', lookup_expr='lte')
    price__from = NumberFilter(field_name='price', lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['title', 'brand', 'price__from', 'price__to']
    #     fields = {
    #         'price': ['gte', 'lte'] # bu oddiy from to kabi chiroyli chiqmaydi, sodda korinishda chiqadi
    # }
