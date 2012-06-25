# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='django-file-storage',
    version='0.1',
    url='http://github.com/meshy/django-file-storage',
    license='LGPL',
    author='Charlie Denton',
    author_email='charlie@meshy.co.uk',
    description='Set file storage as an environment variable in your Django application.',
    long_description=open('README.rst').read(),
    py_modules=('django_file_storage',),
)
