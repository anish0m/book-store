from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Book

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")

    no_of_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_no_of_books": no_of_books,
        "average_rating": avg_rating
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
