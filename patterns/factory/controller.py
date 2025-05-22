from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from patterns.factory.service import Localize


class FactoryController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._localize = Localize()

    def get(self, request):
        # Xử lý logic GET
        data = self._localize.get()
        return Response(data, status=status.HTTP_200_OK)
