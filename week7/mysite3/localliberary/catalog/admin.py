from django.contrib import admin
from .models import Author, BookInstance, Book, Genre, Language


# Register your models here.
# admin.site.register(Author)


class BooksInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
        )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)


#admin.site.register(Author, AuthorAdmin)
#admin.site.register(BookInstance)
#admin.site.register(Book)
#admin.site.register(Genre)
