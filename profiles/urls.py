from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),
]