
from django.contrib import admin
from django.urls import path,include
from abra_project.views import write_message,GetAllMessagesView,GetUnreadMessagesView,ReadMessageOfLoggedInUserView,DeleteMessageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path("users/", include('users.urls') ),
    path('api/write_message/', write_message, name='write_message'),
    path('api/get_all_messages/', GetAllMessagesView.as_view(), name='user-messages'),
    path('api/unread/', GetUnreadMessagesView.as_view(), name='unread-messages'),
    path('api/read_message/<int:message_id>/', ReadMessageOfLoggedInUserView.as_view(), name='read-message'),
    path('api/delete_message/<int:message_id>/', DeleteMessageView.as_view(), name='delete-message'),


]
