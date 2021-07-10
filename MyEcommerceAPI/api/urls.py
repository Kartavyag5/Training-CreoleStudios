from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('products/', ListProduct.as_view(), name='products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='singleproduct'),

    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>', DetailUser.as_view(), name='singleuser'),
    path('users/registration',RegistrationAPIView.as_view(),name='registration'),

#------new Cart---------------------
    path('carts/', CartAPIView.as_view(), name='carts'),
    path('carts/<product_id>', CheckProductInCart.as_view(), name='cartDetails'),

#-------------orders---------------------
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderDetailsView.as_view(), name='orderDetails'),
    path('billing_profile',BillingProfileAPIView.as_view(), name='billing_profiles'),

#---------------payment checkout urls-----------------------
    #path("checkout/", CheckoutView.as_view()),
    #path("hook/", my_webhook_view),
    #path('pay/', start_payment, name="payment"),
    # path('payment/success/', handle_payment_success, name="payment_success"),
    
    #path('test/',test,name='test'),

#----------------Razorpay urls------------------------------
 # Payment APIs
    path('payment/', payment, name = 'payment'),
    # path('handlerequest/', handlerequest, name = 'handlerequest'),
    # # Generating Invoice
    # path('generateinvoice/<int:pk>/', GenerateInvoice.as_view(), name = 'generateinvoice'),

]
