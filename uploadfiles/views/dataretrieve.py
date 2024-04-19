from rest_framework import generics
from django.http import JsonResponse
from ..s3_service import get_pg_data, get_s3_data

class FileDownloadView(generics.RetrieveAPIView):
    def get(self, *args, **kwargs):
        try:
            bucket_name, file = get_pg_data(id=self.kwargs['id'])
            file_content = get_s3_data(bucket_name, file)

            json_response = {
                'bucket': bucket_name,
                'key': file,
                'content': file_content
            }

            return JsonResponse(json_response)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
