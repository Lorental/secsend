from django.urls import path

from .import views

app_name = 'message'

urlpatterns = [
    path('save_message/', views.save_message, name='save_message'),
]
