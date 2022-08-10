from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/details', views.PostView.as_view(), name='post-details'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
    path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
  ]
