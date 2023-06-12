from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


from django.db import models
from slugify import slugify



class Category(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=120, unique=True, primary_key=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория', default='waiting')
    order_id = models.AutoField(primary_key=True)
    description = models.TextField(verbose_name='Описание продукта', blank=True)
    phone_sender = models.CharField(max_length=13)
    phone_receiver = models.CharField(max_length=13)
    address_sender = models.CharField(max_length=100)
    address_receiver = models.CharField(max_length=100)
    price = models.IntegerField(default=200)
    # price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма доставки')
    created_at = models.DateTimeField(auto_now_add=True)
    curier = models.ForeignKey(User, related_name='courier', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.phone_sender} -- {self.order_id}'
    


