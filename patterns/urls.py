from django.urls import path
from patterns.factory.controller import FactoryController

urlpatterns = [
    path("factory", FactoryController.as_view(), name="factory"),
]
