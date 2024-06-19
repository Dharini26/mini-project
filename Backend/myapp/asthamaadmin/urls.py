from django.urls import path
from .views import adminLoginView

urlpatterns = [
    path("adminLogin/",adminLoginView.as_view(),name="adminLogin")
]
