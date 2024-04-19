from django.contrib import admin
from django.urls import path
from uploadfiles.views.datasend import FileUploadView
from uploadfiles.views.dataretrieve import FileDownloadView
from uploadfiles.views.createuser import create_user_view
from uploadfiles.views.loginuser import login_user_view
from uploadfiles.views.getusers import get_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', FileUploadView.as_view()),
    path('download/<int:id>/', FileDownloadView.as_view()),
    path('users/signup/', create_user_view),
    path('users/login/', login_user_view),
    path('users/', get_user_view)
]
