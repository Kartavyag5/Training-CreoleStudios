from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.fields import Field, IntegerField


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class loginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('username','password')


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title')

class ProductSerializer(serializers.ModelSerializer):
    category_name = categorySerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = (
            'id',
            'product_tag',
            'name',
            'price',
            'stock',
            'imageUrl',
            'status',
            'created_at',
            'updated_at',
            'category_name',
        )


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = (
            'id',
            #'product_tag',
            'name',
            #'category_id',
            'price',
            #'stock',
            #'imageUrl',
            #'status',
            #'created_at',
            #'updated_at',
        )
        
   

class CategorySerializer(serializers.ModelSerializer):
    products = CategoryProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'products',
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )

#-----------------new Cart Section-----------------------


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        total = Field(source='total')
        tax_total = Field(source='tax_total')
        total_cart_products = Field(source='total_cart_products')

        fields = ['id', 'user', 'products', 'tax_total', 
                    'total', 'total_cart_products']


#----------------------Billing Profile-------------------------

class BillingProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    country = serializers.SerializerMethodField()

    class Meta:
        model = BillingProfile
        fields = ['id', 'user', 'name', 'phone', 'email', 'address_line_1',
                  'address_line_2', 'city', 'state', 'country_code', 'pincode', 'country']

    def get_country(self, obj):
        return obj.country


#---------------------ORDER SERIALIZERS------------------------------


class OrderSerializer(serializers.ModelSerializer):
    billing_profile = BillingProfileSerializer()
    class Meta:
        model = Order
        grand_total = Field(source='grand_total')
        tax_total = Field(source='tax_total')
        fields = [
            'id',
            #'order_id',
            'order_payment_id',
            'status',
            'billing_profile',
            'created_at',
            'updated_at',
            'shipping_total',
            'cart_total',
            'tax_total',
            'grand_total',
        ]   


class DetailedOrderSerializer(serializers.ModelSerializer):
    billing_profile = BillingProfileSerializer()
    cart = CartSerializer()

    class Meta:
        model = Order
        grand_total = Field(source='grand_total')
        tax_total = Field(source='tax_total')
        fields = [
            'id',
            'billing_profile',
           # 'order_id',
            'cart',
            'status',
            'order_payment_id',
            'created_at',
            'updated_at',
            'shipping_total',
            'cart_total',
            'tax_total',
            'grand_total',
        ]





