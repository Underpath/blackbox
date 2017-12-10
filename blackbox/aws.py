import boto3
import hashlib
import base64
import config


def get_hash():
    md5_hash = hashlib.md5()
    with open(config.ENCRYPTED_FILE_PATH, 'rb') as encrypted_file:
        while True:
            data = encrypted_file.read(config.BLOCKSIZE)
            if not data:
                break
            md5_hash.update(data)
    encoded = base64.b64encode(md5_hash.digest()).decode('utf8')
    digest = md5_hash.hexdigest()
    return encoded, digest


def put_file():
    md5_encoded, md5 = get_hash()
    client = boto3.client(
        's3',
        aws_access_key_id=config.get_option('access_key', 'AWS'),
        aws_secret_access_key=config.get_option('secret_key', 'AWS'),
    )
    metadata = {'md5': md5}

    with open(config.ENCRYPTED_FILE_PATH, 'rb') as encrypted_file:
        try:
            response = client.put_object(Body=encrypted_file, Bucket=config.get_option('bucket', 'AWS'), Key=config.ENCRYPTED_FILENAME, ContentMD5=md5_encoded, Metadata=metadata)
        except Exception:
            print('Error putting file in S3.')
            return False

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    return False
