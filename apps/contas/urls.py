from django.urls import path
from contas import views


urlpatterns = [
    path('timeout/',  views.timeout_view, name='timeout'),
]

