from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        data = response.data if isinstance(
            response.data, list) else [response.data]
        errors = set()
        for item in data:
            for field, error in item.items():
                errors.add(
                    (field, error[0] if isinstance(error, list) else error))
        response.data = {'errors': []}
        for error in errors:
            response.data['errors'].append(dict([error]))
    return response
