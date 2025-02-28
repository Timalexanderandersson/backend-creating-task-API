from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Frontpage api message
def Heyapi(request):
    return JsonResponse({'message': 'This is creating task API'})

# Logout view for clearing cookies
@api_view(['POST'])
def logout_view(request):
    response = Response({'detail': 'Successfully logged out'})
    response.delete_cookie('my-app-auth')
    response.delete_cookie('my-refresh-token')
    response.delete_cookie('csrftoken')
    response.delete_cookie('sessionid')
    return response
