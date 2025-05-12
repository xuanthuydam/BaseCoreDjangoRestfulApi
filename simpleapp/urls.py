from django.urls import path
from simpleapp.controllers.crud_controller import CRUDController

urlpatterns = [
    path("crud", CRUDController.as_view(), name="crud"),
]