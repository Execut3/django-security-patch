# About Package
This Repo with include all security patches, 
That can be used to make django more secure against existing vulnerabilities.

**Note** This repo is not fully updated yet.


## Installation

Install from Python packages repository:

```
pip install django-security-patch
```

Adding to Django Applications's `settings.py` file:

```
INSTALLED_APPS = (
    ...
    'django_security_patch',
)
```

After Django 1.10, middleware modules can be added to MIDDLEWARE list in settings file:

```
MIDDLEWARE = [
    ...
    'django_security_patch.middleware.QueryStringsSanitizer'
]
```

For Pre-Django 1.10, middleware modules can be added to `MIDDLEWARE_CLASSES` in `settings.py` file.




