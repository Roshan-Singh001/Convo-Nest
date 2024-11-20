from django.shortcuts import render, redirect
from django.contrib.auth import logout

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {"current_user": request.user.username}
    return render(request, "chat/chatPage1.html", context)

def logout_view(request):
    logout(request)
    return redirect("login-user")


# def index(request):
#     return render(request, "chat/index.html")


# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})