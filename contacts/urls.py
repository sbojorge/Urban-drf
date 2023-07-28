from django.urls import path
from .views import ContactListCreate, ContactDetail
urlpatterns = [
    path('contacts/', ContactListCreate.as_view()),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
]