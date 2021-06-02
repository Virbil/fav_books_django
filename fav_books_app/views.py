from django.contrib import messages
from fav_books_app.models import *
from django.shortcuts import render, redirect

def books(request):
    logged_user = User.objects.get(id=request.session["userid"])
    uploaded_by = logged_user.books_uploaded.all()
    user_who_favorited = logged_user.favorited_books.all()

    context = {
        "user_info": User.objects.get(id=request.session["userid"]),
        "all_books": Book.objects.all(),
        'all_user_books': uploaded_by,
        'all_favorites': user_who_favorited
    }
    return render(request, "books.html", context)

def new_book(request):
    if request.method == "POST":
        errors = Book.objects.duplicate_check(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        logged_user = User.objects.get(id=request.session["userid"])

        book = Book.objects.create(
            title=request.POST["title"],
            author=request.POST["author"],
            description=request.POST["description"],
            uploaded_by=logged_user
        )
        book.user_who_favorited.add(User.objects.get(id=request.session["userid"]))

    return redirect('/books')

def add_to_favorites(request, book_id):
    if request.method == "POST":
        book_to_favorite = Book.objects.get(id=book_id)
        
        book_to_favorite.user_who_favorited.add(User.objects.get(id=request.session["userid"]))
    return redirect(f'/books/{book_id}')

def book_info(request, book_id):
    logged_user = User.objects.get(id=request.session["userid"])

    context = {
        "user_info": User.objects.get(id=request.session["userid"]),
        "book_info": Book.objects.get(id=book_id)
    }
    return render(request, "book-info.html", context)

def remove_from_favorites(request, book_id):
    if request.method == "POST":
        book_to_favorite = Book.objects.get(id=book_id)
        
        book_to_favorite.user_who_favorited.remove(User.objects.get(id=request.session["userid"]))
    return redirect('/books')

def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect('/books')