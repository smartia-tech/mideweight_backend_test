from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response
    if response is not None:
        customized_response = {"success": False, "message": "request could not be processed", 'errors': []}

        for key, value in response.data.items():
            error = {'field': key, 'message': value}
            customized_response['errors'].append(error)

        response.data = customized_response

    return response

