from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateTimeField, TextField, SmallIntegerField, DecimalField, ForeignKey, \
    CASCADE, SET_NULL, SlugField , ImageField
from django.db.models.functions import Now
from django.utils.text import slugify


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)
    created_at = DateTimeField(auto_now_add=True , db_default=Now())

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(BaseSlugModel):
    pass


class Product(BaseSlugModel):
    price = DecimalField(max_digits=9 , decimal_places=2)
    discount = SmallIntegerField()
    quantity = SmallIntegerField()
    description = TextField()
    image = ImageField(upload_to="products/%y/%m/%d")
    category = ForeignKey('apps.Category' , CASCADE , related_name='products')




class Order(Model):
    user = ForeignKey(User , SET_NULL , blank=True , null=True , related_name='orders')
    product = ForeignKey('apps.Product' , SET_NULL, blank=True , null=True , related_name='orders')
    quantity = SmallIntegerField()
    created_at = DateTimeField(auto_now_add=True , db_default=Now())


