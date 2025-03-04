from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def hey_api(request):
    return Response({'message': 'This is creating task API'})


# Logout view for clearing cookies
@api_view(['POST'])
def logout_view(request):
    # Skapa ett svar för att indikera att användaren har loggat ut
    response = Response({'detail': 'Successfully logged out'})
    response.delete_cookie('my-app-auth', path='/')
    response.delete_cookie('my-refresh-token', path='/')
    response.delete_cookie('csrftoken', path='/')
    response.delete_cookie('sessionid', path='/')
    response.delete_cookie('sessionid')
    
    return response