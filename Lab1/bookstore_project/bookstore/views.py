from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


books = []
book_id_counter = 1


def create_book(request):
    global book_id_counter
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        published_year = request.POST["published_year"]
        book = {"id": book_id_counter, "title": title,
                "author": author, "published_year": published_year}
        books.append(book)
        book_id_counter += 1
        messages.success(request, "Book added successfully.")
        return redirect("home")
    else:
        return render(request, "create_book.html")


def show_book(request, pk):
    book = None
    for b in books:
        if b['id'] == pk:
            book = b
            break
    # book = next((b for b in books if b["id"] == int(pk)), None)
    if book:
        return render(request, "show_book.html", {"book": book})
    else:
        return HttpResponse("Book not found.")


def edit_book(request, pk):
    book = next((b for b in books if b["id"] == int(pk)), None)
    if request.method == "POST":
        if book:
            book["title"] = request.POST["title"]
            book["author"] = request.POST["author"]
            book["published_year"] = request.POST["published_year"]
            messages.success(request, "Book updated successfully.")
            return redirect("list_books")
        else:
            return HttpResponse("Book not found.")
    else:
        if book:
            return render(request, "edit_book_form.html", {"book": book})
        else:
            return HttpResponse("Book not found.")


def delete_book(request, pk):
    book = next((b for b in books if b["id"] == int(pk)), None)
    if request.method == "POST":
        if book:
            books.remove(book)
            messages.success(request, "Book deleted successfully.")
            return redirect("list_books")
        else:
            return HttpResponse("Book not found.")
    else:
        if book:
            return render(request, "delete_book.html", {"book": book})
        else:
            return HttpResponse("Book not found.")


def list_books(request):
    return render(request, "list_books.html", {"books": books})
