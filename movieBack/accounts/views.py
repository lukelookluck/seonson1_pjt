from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer
# Create your views here.

# serializer.like_movie.join(request.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request):
		# print(request.data.values)
		serializer = UserSerializer(instance=request.user, data=request.data, partial=True)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			# print(serializer)	
			return Response(serializer.data)
			# return render(request, '/' )