from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .models import Message
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write_message(request):
    serializer = MessageSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        messages = Message.objects.filter(receiver=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    
class GetUnreadMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        unread_messages = Message.objects.filter(receiver=request.user, read=False)
        serializer = MessageSerializer(unread_messages, many=True)
        return Response(serializer.data)


class ReadMessageOfLoggedInUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, message_id, *args, **kwargs):
        message = get_object_or_404(Message, id=message_id, receiver=request.user)
        message.read = True
        message.save(update_fields=['read'])
        serializer = MessageSerializer(message)
        return Response(serializer.data)


from django.db.models import Q

class DeleteMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, message_id, *args, **kwargs):
        message = get_object_or_404(Message, Q(sender=request.user) | Q(receiver=request.user), id=message_id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
