from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view()),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:post_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('<int:post_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),

]
