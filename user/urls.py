from django.urls import path
from .views import index

app_name = 'user'

urlpatterns = [
    path('home', index.as_view() ,name = 'home' ),
 
]
