from django.urls import path    
from . import views
urlpatterns = [
    path('get-all-users', views.get_all_users , name='get_all_users'),
]