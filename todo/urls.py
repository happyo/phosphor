from django.urls import path

from .views import ItemView

app_name = 'todo'
urlpatterns = [
    path('<str:username>/todo/', ItemView.as_view(), name='list'),
]
