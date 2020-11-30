from django.urls import path
from fileUploader.views import UploadFile


urlpatterns = [
    path('', UploadFile.as_view())
]
