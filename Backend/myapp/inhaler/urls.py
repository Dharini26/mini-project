from django.urls import path
from .views import InhalerView,UserByName

urlpatterns = [
    path("inhale/",InhalerView.as_view(),name="inhale"),
    path("username/<username>",UserByName.as_view(),name="username"),
]
