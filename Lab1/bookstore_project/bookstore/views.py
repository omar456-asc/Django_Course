from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

books = []


def create_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        published_year = request.POST["published_year"]
        book = {"title": title, "author": author,
                "published_year": published_year}
        messages.success(request, "Book added successfully.")
        return redirect("home")
        # return HttpResponse("Book added successfully.")
    else:
        return render(request, "create_book.html")


def show_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        book = next((b for b in books if b["title"] == title), None)
        if book:
            return render(request, "show_book.html", {"book": book})
        else:
            return HttpResponse("Book not found.")
    else:
        return render(request, "show_book_form.html")


def edit_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        book = next((b for b in books if b["title"] == title), None)
        if book:
            book["title"] = request.POST["new_title"]
            book["author"] = request.POST["new_author"]
            book["published_year"] = request.POST["new_published_year"]
            return HttpResponse("Book updated successfully.")
        else:
            return HttpResponse("Book not found.")
    else:
        return render(request, "edit_book_form.html")


def delete_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        book = next((b for b in books if b["title"] == title), None)
        if book:
            books.remove(book)
            return HttpResponse("Book deleted successfully.")
        else:
            return HttpResponse("Book not found.")
    else:
        return render(request, "delete_book_form.html")


def list_books(request):
    return render(request, "list_books.html", {"books": books})
