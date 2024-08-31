from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_data = {
            'username': user.username,
            'email': user.email,
            # Add more user-specific fields if necessary
        }
        return Response({
            'message': 'Welcome to the JWT Authentication page!',
            'user': user_data
        }, status=status.HTTP_200_OK)