from django.urls import path
from . import views

urlpatterns = [
  path('hello/', views.say_hello),
  path('block_number/', views.get_current_block)
]