from django.urls import path
from .views import ServiceListCreate, ServiceDetailList

urlpatterns = [
    path('services/', ServiceListCreate.as_view()),
    path('services/<int:pk>/', ServiceDetailList.as_view()),
]
