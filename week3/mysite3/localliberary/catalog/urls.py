from django.urls import path
from . import views

urlpatterns = [
            # path('', views.catalog_home, name='catalog'),
            path('', views.index, name='index'),
            path('books/', views.BookListView.as_view(), name='books'),
            path('book/<int:pk>', views.BookDetailListView.as_view(),name = 'book-detail'),
]
