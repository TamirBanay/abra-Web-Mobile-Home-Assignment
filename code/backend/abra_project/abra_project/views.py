from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write_message(request):
    # request.user is the sender and is already authenticated
    serializer = MessageSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
