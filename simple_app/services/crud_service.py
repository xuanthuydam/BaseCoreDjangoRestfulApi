class CRUDService():
    def get(self, request):
        return {"message": "GET request received"}

    def post(self, request):
        return {"message": "POST request received", "payload": request.data}

    def put(self, request):
        return {"message": "PUT request received", "payload": request.data}

    def delete(self, request):
        return {"message": "DELETE request received"}
