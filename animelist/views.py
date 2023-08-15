from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    AnimeList, Category, Type
)
from .serializers import (
    AnimeListSerializer,
    
    TypeSerializer,
    
    CategorySerializer,
)


class AnimeListView(APIView):
    permission_classes = [permissions.AllowAny, ]
    
    def get(self, request):
        anime_list = AnimeList.objects.all()
        serializer = AnimeListSerializer(anime_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
