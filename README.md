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


## Description

One the leading vulnerabilities in current web application is `Template Injeciton`. For example
When u are using aa javascript library like Angularjs, You should be careful that data reflected
from user (from search box for example) will not be rendered in the context that there is another
template handler (like angularjs) which will lead to `Template Injection`.

for example user sends `[[test]]` via search box of django. this will of course will not create 
any vulnerability for django, but if this value is rendered in template and there is angularjs, 
it will give attacker to do some Client-side Attacks.


## Usage

just install package and add this in your settings.py file:

```
QUERY_REMOVE_STRINGS = ['{{', '}}', '[[', ']]']
```

From now on, any query string in request.GET that includes this characters, will be replaced.