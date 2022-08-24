
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Language, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RenewBookForm
from catalog.models import Author, Book


# Create your views here.


def catalog_home(request):
    return HttpResponse("welcome to Liberary Catalog Home!!!")


def index(request):
    """View function for home page of site."""

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

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
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


class BookListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book
    # Specify your own template name/location
    template_name = 'my_arbitrary_template_name_list.html'


class BookDetailListView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Author
    template_name = 'author.html'


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAndBorrowerListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to all users"""
    model = BookInstance
    template_name = 'catalog/all_borrowed_book_list.html'
    paginate_by = 10
    # Or multiple permissions
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')


class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Author
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')


class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')


class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary',
              'borrower', 'isbn', 'genre', 'language']
    success_url = reverse_lazy('books')
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')


class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = ('catalog.can_mark_returned',
                           'catalog.can_edit')
