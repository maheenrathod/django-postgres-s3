from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.users import CustomUser
from ..serializers import UserSerializer

@api_view(['GET'])
def get_user_view(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)