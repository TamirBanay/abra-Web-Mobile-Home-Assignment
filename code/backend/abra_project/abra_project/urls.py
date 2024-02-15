
from django.contrib import admin
from django.urls import path,include
from abra_project.views import write_message,GetAllMessagesView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path("users/", include('users.urls') ),
    path('write_message/', write_message, name='write_message'),
    path('get_all_messages/', GetAllMessagesView.as_view(), name='user-messages'),

]
