from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from patterns.builder.house.service import BuilderService


class BuilderController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._builder_service = BuilderService()

    def get(self, request):
        # Xử lý logic GET
        data = self._builder_service.get()
        return Response(data, status=status.HTTP_200_OK)
