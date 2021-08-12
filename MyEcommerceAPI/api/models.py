from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from EcommerceAPI.utils import unique_product_id_generator
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import stripe

# Create your models here.

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
        

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField(blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tax = models.DecimalField(max_digits=4, decimal_places=2, default=18)
    
    def __str__(self):
        return '{}: {}'.format(self.product_tag, self.name)

#-------------------New Cart Section----------------------------

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)    
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{str(self.user)}: {str(self.created_at)[0:19]}"

    @property
    def total(self):
        total = 0
        for item in self.products.all():
            total += int(item.quantity) * float(item.product.price)
        return total

    @property
    def tax_total(self):
        total = 0
        for item in self.products.all():
            total += int(item.quantity) * float(item.product.price) * \
                float(item.product.tax) / 100
        return total

    @property
    def total_cart_products(self):
        return sum(item.quantity for item in self.products.all())


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}: {str(self.cart)[0:21]}"


#------------------billing profile---------------------------





class BillingProfile(models.Model):
    class CountriesChoises(models.TextChoices):      
        GG = 'GG', 'Guernsey'
        GN = 'GN', 'Guinea'
        GW = 'GW', 'Guinea-Bissau'
        GY = 'GY', 'Guyana'
        HT = 'HT', 'Haiti'
        HM = 'HM', 'Heard Island and McDonald Islands'
        VA = 'VA', 'Holy See'
        HN = 'HN', 'Honduras'
        HK = 'HK', 'Hong Kong'
        HU = 'HU', 'Hungary'
        IS = 'IS', 'Iceland'
        IN = 'IN', 'India'

    stripe_customer_id = models.CharField(
        max_length=100, blank=True, null=True)   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country_code = models.CharField(
        choices=CountriesChoises.choices, max_length=2, default=CountriesChoises.IN)
    pincode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.user.username

    @property
    def country(self):
        return self.CountriesChoises(self.country_code).label




#--------------------New Order Section-------------------------


STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)





class Order(models.Model):
    billing_profile = models.ForeignKey(
        BillingProfile, on_delete=models.CASCADE, null=True, blank=True)
    #order_id = models.CharField(max_length=120, blank=True,)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='created', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shipping_total = models.DecimalField(
        default=70, max_digits=10, decimal_places=2)
    order_payment_id = models.CharField(max_length=100, null=True, blank=True)

    
    #exclude=("order_id",)
    def __str__(self):
        return f"{str(self.cart)[0:9]}  {str(self.cart)[9:28]}"

    @property
    def cart_total(self):
        return self.cart.total

    @property
    def tax_total(self):
        return self.cart.tax_total

    @property
    def grand_total(self):
        grand_total = float(self.cart_total) + float(self.tax_total) + float(self.shipping_total)
        return grand_total


