from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import logout

@api_view(['GET'])
def hey_api(request):
    return Response({'message': 'This is creating task API'})


@api_view(['POST'])  
def custom_logout(request):
    if request.user.is_authenticated: 
        logout(request) 

    response = JsonResponse({"message": "Utloggad"})
    response.delete_cookie('my-app-auth') 
    response.delete_cookie('my-refresh-token')
    response.delete_cookie('csrftoken')
    response.delete_cookie('sessionid') 
    return response