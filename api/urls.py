from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .yasg import urlpatterns as url_doc


# router = DefaultRouter()


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-user'), 
    path('login/', views.LoginApiView.as_view(), name='login-user'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('', include(router.urls)),  
]   


urlpatterns += url_doc
