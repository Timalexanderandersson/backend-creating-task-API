from django.http import JsonResponse

# Frontpage api message
def Heyapi(request):
    return JsonResponse({'message': 'This is creating task API'})