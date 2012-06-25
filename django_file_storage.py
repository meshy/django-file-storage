import os


backends = {
    'cloudfront': 'cloudfront.cloudfrontstorage.CouldFrontStorage',
    's3boto': 'storages.backends.s3boto.S3BotoStorage',
}


default_backend = 'django.core.files.storage.FileSystemStorage'


def config(default=default_backend):
    try:
        return backends[os.environ.get('DEFAULT_FILE_STORAGE')]
    except KeyError:
        return default
