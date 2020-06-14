from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import FollowerSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def follows(request,username):
    User = get_user_model()
    target_user = User.objects.get(username=username)
    print(target_user.username)
    print('###################################')
    serializer = FollowerSerializer(target_user)
    return Response(serializer.data)

