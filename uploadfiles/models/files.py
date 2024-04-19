from django.db import models
import os

def dynamic_upload_path(instance, filename):
        return os.path.join(instance.folder, filename)

class FileUpload(models.Model):
    file = models.FileField(upload_to=dynamic_upload_path)
    filename = models.CharField(max_length=255, default='')
    folder = models.CharField(max_length=255, default='other')
    s3_bucket = models.CharField(max_length=255, default='django-postgres-s3')
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'uploaded_files'