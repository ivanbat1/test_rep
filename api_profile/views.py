from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import UserProfileSerializers
from .models import UserAPI


class TestApiList(APIView):
    """Test API view"""
    serializer_class = UserProfileSerializers

    def get(self, request):
        """Get all profiles use API"""
        form = UserProfileSerializers()
        return Response({'serializer': UserAPI.objects.all(), 'form': form}, template_name='test.html')

    def post(self, request):
        """method create new user"""
        print(request.data['img'])
        serializer = self.serializer_class(data=request.data)
        print('tyt')
        if serializer.is_valid():
            print('yge tyt')
            form = UserProfileSerializers()
            serializer.save()
            return Response({'serializer': UserAPI.objects.all(), 'form': form}, template_name='test.html')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TestApiDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """

    def get_object(self, pk):
        try:
            return UserAPI.objects.get(pk=pk)
        except UserAPI.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """method get user on id"""
        snippet = self.get_object(pk)
        form = UserProfileSerializers()
        serializer = UserProfileSerializers(snippet)
        return Response({'serializer': serializer.data, 'form': form}, template_name='test_detail.html')

    def post(self, request, pk):
        """method update user on id"""
        snippet = self.get_object(pk)
        serializer = UserProfileSerializers(snippet, data=request.data)
        if serializer.is_valid():
            form = UserProfileSerializers()
            serializer.save()
            return Response({'serializer': serializer.data, 'form': form}, template_name='test_detail.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """method delete user on id"""
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
