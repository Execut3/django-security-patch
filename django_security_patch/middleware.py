import logging

from . import settings
from django.utils.http import is_safe_url


def QueryStringsSanitizer(get_response):
    def wrapper(request):
        if not request.method == 'GET':
            response = get_response(request)
            return response

        # This method will only be applied to GET requests
        # Only apply this method on GET requests
        query_strings = []

        # Now iterate on all GET query params
        for (key, value) in dict(request.GET.lists()).items():

            try:
                tmp_value = value[0]

                # replace not allowed strings with '' for each querystring value.
                for rm in settings.QUERY_REMOVE_STRINGS:
                    # Value is it list for example:
                    # ?name=test   with be received here in format: {'name': ['test']}
                    tmp_value = tmp_value.replace(rm, '')
            except Exception as e:
                # Ignore if any error happened
                # TODO: Check situations that lead to here, may cause some leaks!
                logging.error(str(e))
                continue

            # Here we check if this value is the return-link,
            # If so do some validations on it to protect open-redirect bug!
            if key == settings.REDIRECT_URL_VARIABLE:
                # Here means user sent variable redirect-url,
                # So just validate it with django core functions
                # And filter all not valid data from it and put back
                # Again on the request.
                redirect_url = tmp_value
                is_valid = is_safe_url(
                    url=redirect_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure(),
                )
                tmp_value = "/" if not is_valid else redirect_url

            # Now cleaned data push to final list
            query_strings.append((key, tmp_value))

        edit_get = request.GET.copy()
        # Get a copy of request.GET and update filtered values to new ones.
        for i in range(len(query_strings)):
            edit_get[query_strings[i][0]] = query_strings[i][1]

        # Rebuild GET request again and return it
        request.GET = edit_get
        response = get_response(request)

        return response

    return wrapper
