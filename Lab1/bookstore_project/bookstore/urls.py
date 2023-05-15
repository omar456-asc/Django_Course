from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('create/', views.create_book, name='book_create'),
    path('<int:pk>/', views.show_book, name='book_detail'),
    path('<int:pk>/edit/', views.edit_book, name='book_edit'),
    path('<int:pk>/delete/', views.delete_book, name='book_delete'),
]
