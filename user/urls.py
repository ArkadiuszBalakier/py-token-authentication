from django.contrib.auth.views import LoginView
from django.urls import path

from user.views import CreateUserView, LoginUserView, ManageUserView

app_name = 'user'

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path('token-auth/', LoginUserView.as_view(), name='token-auth'),
    path("me/", ManageUserView.as_view(), name="manage"),
]