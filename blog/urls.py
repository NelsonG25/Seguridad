from django.urls import path
from .views import login, index

urlpatterns = [
    path('', login, name="login"),
    path('index/', index, name="index"),
]