from django.urls import path
from .views import RegisterUserView, LogoutView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'refresh_token'),
    path('protected_route/', ProtectedView.as_view(), name='protected'),
    path('logout/', LogoutView.as_view(), name='logout')
]