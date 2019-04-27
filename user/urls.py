from django.urls import path

from .views import LoginView, RegisterView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('join/', RegisterView.as_view(), name='join'),
]
