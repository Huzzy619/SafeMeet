from django.urls import path
from .apis import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register" ),
]