from django.db.models import Model, CharField, PositiveIntegerField, TextField, JSONField, ForeignKey, CASCADE, \
    PositiveSmallIntegerField, ImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(Model):
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    price = PositiveIntegerField(default=0)
    brand = CharField(max_length=255, null=True, blank=True)
    specification = JSONField(null=True, blank=True)
    category = ForeignKey(Category, CASCADE, related_name='products')
    discount = PositiveSmallIntegerField(default=0)

    @property
    def discount_price(self):
        return self.price - self.price * self.discount / 100


class ProductImage(Model):
    image = ImageField(upload_to='products/', null=True, blank=True)
    product = ForeignKey(Product, CASCADE, related_name='images')
