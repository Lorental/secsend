from django.urls import path

from .import views

app_name = 'message'

urlpatterns = [
    path('', views.show_index, name='show_index'),
    path('<str:identificator>', views.show_message, name='show_message'),
    path('save_message/', views.save_message, name='save_message'),
]
