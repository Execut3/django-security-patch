import re
from setuptools import setup
from os import path

project_path = path.abspath(path.dirname(__file__))

with open(path.join(project_path, 'README.md')) as f:
    long_description = f.read()

setup(
    name='django-security-patch',
    packages=['django_security_patch'],
    license='GPT',
    version='0.0.1',
    description='Includes some security patches for better security in Django applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Reza Torkaman Ahmadi',
    author_email='execut3.binarycodes@gmail.com',
    url='https://github.com/Execut3/django-security-patch',
    keywords=['django', 'security'],
    classifiers=[
        "Framework :: Django"
    ],
)
