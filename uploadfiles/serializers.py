from rest_framework import serializers
from uploadfiles.models.files import FileUpload
from uploadfiles.models.users import CustomUser

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['file', 'filename', 'folder', 's3_bucket', 'upload_timestamp']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']