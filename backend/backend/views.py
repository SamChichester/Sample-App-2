from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class MessageAPIView(APIView):
    def get(self, request):
        return Response("Hello from Django!", status=status.HTTP_200_OK)