from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.utils import timezone

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    response = exception_handler(exc, context)

    # If DRF was able to handle the exception (response is not None)
    if response is not None:
        # Extract the original error details
        if isinstance(response.data, dict):
            message = response.data
        else:
            # If the response data is not a dictionary, 
            # convert it to a dictionary with a 'detail' key
            message = {'detail': str(response.data)}
            
        # Customize the response data
        custom_response_data = {
            'status_code': response.status_code,
            'message': message,
            'error': True,
            'success': False,
            'timestamp': timezone.now().isoformat()
        }
        return Response(custom_response_data, status=response.status_code)

    return response