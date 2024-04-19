from rest_framework.parsers import MultiPartParser, FormParser
from ..serializers import FileSerializer
from uploadfiles.models.files import FileUpload
from rest_framework import generics

class FileUploadView(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def create_path(self, serializer):
        folder = self.request.data.get('folder', 'other')
        file = self.request.data['file']
        filename = self.request.data['file'].name
        bucket_name = 'django-postgres-s3'
        instance = serializer.save(file=file, filename=filename, bucket_name=bucket_name)
        instance.folder = folder
        instance.save()

