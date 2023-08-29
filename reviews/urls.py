from django.urls import path
from .views import ReviewListCreate, ReviewDetail

urlpatterns = [
    path('reviews/', ReviewListCreate.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
]