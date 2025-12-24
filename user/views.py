from user.models import User
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.filter(is_available=True)
    return JsonResponse({'available': len(users)})



