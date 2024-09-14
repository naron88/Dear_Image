import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY_ID = "s3-access-key"
ACCESS_SECRET_KEY = "s3-secret-key"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def s3Connection():
    s3 = boto3.client(
        service_name= "s3",
        aws_access_key_id = os.getenv('ACCESS_KEY_ID'),
        aws_secret_access_key = os.getenv('ACCESS_SECRET_KEY'),
        region_name = "ap-northeast-2",
    )
    return s3


def allowedFile(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
