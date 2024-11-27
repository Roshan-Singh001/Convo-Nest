from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
    path("auth/login/", LoginView.as_view(template_name="chat/login.html"), name="login-user"),
    path("auth/logout/", chat_views.logout_view, name="logout-user"),
    path("auth/signup/", LoginView.as_view(template_name="chat/signup.html"), name="sign_up"),
]