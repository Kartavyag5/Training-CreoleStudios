from django.shortcuts import render
from rest_framework.generics import *
from django.views.generic import *
from django.contrib.auth.models import User
from .models import *
from .permissions import *
from .serializers import *
from rest_framework.permissions import *
from rest_framework.response import Response

from rest_framework import status
from rest_framework import serializers
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from EcommerceAPI.settings import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

from django.contrib.auth.decorators import login_required

import json
import razorpay
import stripe
import environ
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.db.models.signals import post_save


class RegistrationAPIView(GenericAPIView):

    serializer_class = RegistrationSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    ordering_fields = '__all__'
    search_fields = '__all__'

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListUser(ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'

class DetailUser(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, IsOwner)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    #search_fields = '__all__'
    #ordering_fields = '__all__'

class ListCategory(ListCreateAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^title','id']
    ordering_fields = ['title']

class DetailCategory(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ListProduct(ListCreateAPIView):    
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['id','^product_tag','^name']
    ordering_fields = '__all__'

class DetailProduct(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    


#-------------------new Cart section------------------------


class CartAPIView(ListCreateAPIView):
    permission_classes = [IsOwner, IsAdminUser]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['id','^user']
    ordering_fields = '__all__'

class CheckProductInCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, product_id, **kwargs):
        product_obj = get_object_or_404(Product, pk=product_id)
        cart_obj, created = Cart.objects.get_existing_or_new(request)
        return Response(not created and CartItem.objects.filter(cart=cart_obj, product=product_obj).exists())


#----------------Billing Profile--------------------------

class BillingProfileAPIView(ListAPIView):
    permission_classes = [IsOwner]
    serializer_class = BillingProfileSerializer
    #queryset = BillingProfile.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        self.request.POST.user = self.request.user
        return self.request.user.billingprofile_set.all()

 # Make The Profile And If Any required field is empty then return 400 error
    def create(self, request, *args, **kwargs):
        # Get The Request Data
        name = request.data.get('name')
        email = request.data.get('email')
        address_line_1 = request.data.get('address_line_1')
        address_line_2 = request.data.get('address_line_2')
        city = request.data.get('city')
        state = request.data.get('state')
        country = request.data.get('country')
        pincode = request.data.get('pincode')

        try:
            profile = self.request.user.billingprofile_set.create(
                name=name,
                email=email,
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                state=state,
                country_code=country,
                pincode=pincode
            )
        except IntegrityError as err:
            return Response({"error": "Insufficient Data"}, status=400)

        # If Everything goes smooth then return the profile
        return Response(self.serializer_class(profile).data)


#--------------------Orders Section-------------------------

class OrderListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['^status','id']
    ordering_fields = '__all__'

class OrderDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailedOrderSerializer
    queryset = Order.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['status','id']
    ordering_fields = '__all__'



#-----------Razor Pay Integration----------------------------

def payment(request):
    if request.user.is_authenticated:
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        
        # get cart data of logged in user
        cart = Cart.objects.filter(user=request.user)
        for item in cart:           
            cartID=item.id
            int_total=item.total            
            user=item.user.first_name +" "+ item.user.last_name
            created_at=item.created_at

        order = Order.objects.filter(cart = cartID)
        for item in order:
            order_id = item.id
            shipping_total = item.shipping_total
            tax_total = item.tax_total
            grand_total = item.grand_total
            status = item.status
            
            
    order_amount = int(grand_total)   # amount must be in Paisa
    order_currency = 'INR'

    payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id = payment_order['id']
    Order.objects.filter(cart=cartID).update(order_payment_id=payment_order_id)

    if payment_order_id != None:
        Order.objects.filter(cart=cartID).update(status=STATUS_CHOICES[1])
        
        
    context = {
        'order_id':order_id,
        'amount':order_amount,
        'api_key':RAZORPAY_KEY_ID,
        'payment_order_id':payment_order_id,
        'username': user,
        'cart_total':int_total,
        'shipping_total':shipping_total,
        'tax_total':tax_total,
        'grand_total':grand_total,
        'created_at': created_at,
        'status': status,
        
    }
    return render(request,'pay.html',context)



#-------------------Testing Purpose-------------------------

# def test(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user)
#         for item in cart:
#             cartID=item.id,
#             total=item.total,
#             user=item.user.username,
#             created_at=item.created_at,

#         order = Order.objects.filter(cart = cartID)    
                   
#         return HttpResponse(cartID)
        
#     else:
#         return HttpResponse("object not found")



