from django.urls import path
from .views import RegisterAPI
from knox import views as knox_views

app_name = 'user'

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view() , name = "Login"),
    # path('api/logout/', knox_views.LogoutView.as_view() , name = 'Logout'),
    # path('api/logoutall/',knox_views.LogoutAllVew.as_view() , name = 'LogoutAll'),
]
