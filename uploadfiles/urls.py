from django.urls import path
from .views.datasend import FileUploadView
from .views.dataretrieve import FileDownloadView
from .views.createuser import create_user_view
from .views.loginuser import login_user_view
from .views.getusers import get_user_view
from .views.helloworld import hello_world

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('download/<int:id>/', FileDownloadView.as_view()),
    path('users/signup/', create_user_view),
    path('users/login/', login_user_view),
    path('users/', get_user_view),
    path('hello/', hello_world)
]