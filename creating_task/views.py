from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def hey_api(request):
    return Response({'message': 'This is creating task API'})



