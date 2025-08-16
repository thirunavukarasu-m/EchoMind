from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

class Ping(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": 'Pong'}, status=status.HTTP_200_OK)

class ProtectedPing(APIView):
    def get(self, request):
        return Response({'message': "protected route"}, status=status.HTTP_200_OK)
