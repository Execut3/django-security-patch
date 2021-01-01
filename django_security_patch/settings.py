from django.conf import settings


# One of the most critical web app bugs, is open redirect which attacker
# Can redirect user to proper page he wants (mostly create fishing attacks.)
# So if below variable is set, whenever a get query with name below happens,
# Will automatically validate it.
REDIRECT_URL_VARIABLE = getattr(settings, 'REDIRECT_URL_VARIABLE', 'redirect_url')

# These are the values which if they occur in request GET query params,
# Will be ignored. For example ?name={{test}} will be rendered to ?name=test
# This we can filter on XSS attacks, SSTI and other....
QUERY_REMOVE_STRINGS = getattr(settings, 'QUERY_REMOVE_STRINGS', ['{', '}', '[', ']'])
