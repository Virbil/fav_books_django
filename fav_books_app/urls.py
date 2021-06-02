from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('new_book', views.new_book),
    path('add_to_favorites/<int:book_id>', views.add_to_favorites, name="add_to_favorites"),
    path('<int:book_id>', views.book_info, name="book_info"),
    path('remove_from_favorites/<int:book_id>', views.remove_from_favorites, name="remove_from_favorites"),
    path('delete/<int:book_id>', views.delete_book),
]