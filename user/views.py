from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({
                'access' : str(token.access_token),
                'refresh' : str(token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': 'Accessed protected route!'
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            refresh = request.data['refresh']
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'message': 'Logout Successful!'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)