from django.urls import path, include

urlpatterns = [
    path('uploadfiles/', include('uploadfiles.urls'))
]