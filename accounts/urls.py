from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # your custom login (optional)
    path('profile/', ProfileView.as_view(), name='profile'),

    # 🔐 JWT built-in token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login using SimpleJWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # get new access token using refresh
]
