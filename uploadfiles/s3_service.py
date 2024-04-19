from uploadfiles.models.files import FileUpload
import boto3

def get_pg_data(id):
    obj = FileUpload.objects.get(id=id)

    #get bucket name and file (key) from pgadmin
    bucket_name = obj.s3_bucket
    file = obj.file.name

    return bucket_name, file

def get_s3_data(bucket_name, file):
    client = boto3.client('s3')

    #get file content using bucket and file name. method used in FileDownloadView
    response = client.get_object(Bucket=bucket_name, Key=file)
    file_content = response['Body'].read().decode('utf-8')

    return file_content