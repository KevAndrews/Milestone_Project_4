"""
URLs for Home App
"""
from django.urls import path
from home.views import Index

urlpatterns = [
    path('', Index.as_view()),
]
