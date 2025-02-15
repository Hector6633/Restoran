from django.urls import path
from . import views
urlpatterns = [
    path('booking', views.book_a_table, name='book_a_table'),
    path('service', views.service, name='service'),
    path('menu', views.menu, name='menu'),
]
