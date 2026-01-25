from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # DEFAULT PAGE
    path('base/', views.base, name='base'), # optional
]
