from django.urls import path
from .views import LoginView, logout_func, RegistrationView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_func, name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
