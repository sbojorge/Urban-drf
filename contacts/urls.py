from django.urls import path
from .views import ContactListCreate, ContactDetailDetail

urlpatterns = [
    path('comments/', ContactListCreate.as_view()),
    path('comments/<int:pk>/', ContactDetail.as_view()),
]