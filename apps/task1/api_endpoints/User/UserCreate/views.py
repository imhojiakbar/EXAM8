from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task1.api_endpoints.User.UserCreate.serializers import UserCreateSerializer
from apps.task1.models import User


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.avatar = request.FILES['avatar']
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={'detail': "Check your inbox we have sent an activation link"})
    # queryset = User.objects.all()
    # serializer_class = UserCreateSerializer
    # parser_classes = [MultiPartParser, FormParser, JSONParser]


__all__ = ('UserCreateView',)