from django.urls import path
from expense_tracker import views

urlpatterns = [
    path("", views.view_prototype),
]