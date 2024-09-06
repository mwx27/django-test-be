from django.urls import path
from . import views

urlpatterns = [
  path('', views.say_hello),
  path('block_number/', views.get_current_block),
  path('balance', views.get_balance),
]