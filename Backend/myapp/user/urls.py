from django.urls import path
from .views import userRegisterView,UserByName,UserLoginView,UpdateInhaler,RefillInhaler

urlpatterns = [
    path("userreg/",userRegisterView.as_view(),name="userreg"),
    path("username/<username>/",UserByName.as_view(),name="username"),
    path("userLogin/",UserLoginView.as_view(),name="userLogin"),
    path("consume/<username>/",UpdateInhaler.as_view(),name="consume"),
    path("refill/<username>/",RefillInhaler.as_view(),name="refill"),
]
