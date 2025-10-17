from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, ChatMessage

def home(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = ChatMessage.objects.filter(room=room).order_by('timestamp')[:50]
    
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'messages': messages,
    })