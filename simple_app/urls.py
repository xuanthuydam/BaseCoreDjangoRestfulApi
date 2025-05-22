from django.urls import path
from simple_app.controllers.crud_controller import CRUDController

urlpatterns = [
    path("crud", CRUDController.as_view(), name="crud"),
]
