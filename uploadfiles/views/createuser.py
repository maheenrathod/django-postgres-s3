from ..serializers import UserSerializer
from ..models.users import CustomUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['POST']) 
def create_user_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        #user authentication for new users
        user = CustomUser.objects.get(email=request.data['email'])
        #returns hash version of password
        user.set_password(request.data['password'])
        user.save()
        #token created -- can be used by react to make api calls
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)