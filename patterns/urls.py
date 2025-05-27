from django.urls import path

from patterns.builder.example.controller import BuilderController
from patterns.builder.house.controller import \
    BuilderController as BuilderControllerHouse
from patterns.factory.controller import FactoryController

urlpatterns = [
    path("factory", FactoryController.as_view(), name="factory"),
    ## builder
    path("builder/example", BuilderController.as_view(), name="builder-example"),
    path("builder/house", BuilderControllerHouse.as_view(), name="builder-house"),
]
