from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from simple_app.services.crud_service import CRUDService


class CRUDController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._crud_service = CRUDService()

    def get(self, request):
        # Xử lý logic GET
        data = self._crud_service.get(request)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Xử lý logic POST
        data = self._crud_service.post(request)
        return Response(data, status=status.HTTP_201_CREATED)

    def put(self, request):
        # Xử lý logic PUT
        data = self._crud_service.put(request)
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        # Xử lý logic DELETE
        data = self._crud_service.delete(request)
        return Response(data, status=status.HTTP_204_NO_CONTENT)
