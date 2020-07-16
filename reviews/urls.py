from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('reviews/upload', views.upload_review_data, name='upload_review_data'),
]