from django.contrib import admin
from django.urls import include, path
#from rest_framework.authtoken.views import obtain_auth_token
from api.views import RegistrationAPIView
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    #path('api/token_varify/',TokenVerifyView.as_view(),name='varify-token'),   
    #path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    #path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    #path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),

]
