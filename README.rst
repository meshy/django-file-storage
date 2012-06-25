django-file-storage
~~~~~~~~~~~~~~~~~~~

Usage
-----

Configure your file storage in ``settings.py``::

    DEFAULT_FILE_STORAGE = django_file_storage.config()

Looks for ``DEFAULT_FILE_STORAGE`` in your environment variables, and falls
back to django's default. The environment variable must be one of those defined
in ``backends``.
