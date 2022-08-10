from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Language, Genre
from django.views import generic

# Create your views here.


def catalog_home(request):
    return HttpResponse("welcome to Liberary Catalog Home!!!")


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genre_contains_word = Genre.objects.filter(
        name__exact='Religions').count()

    num_books_contains_word = Book.objects.filter(
        title__exact='Magmuu-Alfatawah').count()

    title = 'A new Local Library'

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'title': title,
        'num_genre_contains_word': num_genre_contains_word,
        'num_books_contains_word': num_books_contains_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book

    # your own name for the list as a template variable
    #context_object_name = 'book_list'

    # Get 5 books containing the title Street
    #queryset = Book.objects.filter(title__icontains='Street')[:5]

    # Specify your own template name/location
    template_name = 'my_arbitrary_template_name_list.html'

    # def get_query_sets(self):
    #     # Get 5 books containing the title war
    #     return Book.objects.filter(title__icontains='war')[:5]
    #
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailListView(generic.DetailView):
    model = Book
