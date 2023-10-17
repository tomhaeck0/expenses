from django.urls import path
from expense_tracker import views

urlpatterns = [
    path("upload_transfers/", views.upload_transfers),
    path("", views.view_prototype),

]