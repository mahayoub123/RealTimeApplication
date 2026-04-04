from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.utils.text import slugify

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('rooms')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'core/rooms.html', {'rooms': rooms})
    


@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = room.messages.all()

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Message.objects.create(
                room=room,
                user=request.user,
                content=content
            )
            return redirect('room', slug=room.slug)

    return render(request, 'core/room.html', {
        'room': room,
        'messages': messages
    })



@login_required
def create_room(request):

    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            room = Room.objects.create(
                name=name,
                slug=slugify(name)
            )
            return redirect('rooms')  

    return render(request, 'core/create_room.html')