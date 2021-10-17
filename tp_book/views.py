from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from tp_book.models import Book
from tp_book.seriallizers import BookModelSeriallizer, BookSeriallizer


class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all().order_by('-created_at')
        serializers = BookModelSeriallizer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def allApi(request):
    if request.method == 'GET':
        query = Book.objects.all().order_by('-created_at')
        serializer = BookSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = Book.objects.filter(fav=True)
        serializer = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateFavData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializer = BookModelSerializer(query, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostModelData(APIView):
    def post(self, request):
        serializer = BookModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def SetData(request):
    if request.method == 'POST':
        serializer = BookModelSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.data.get('Author')
            store_name = serializer.data.get('store_name')
            description = serializer.data.get('description')
            image = request.FILES['image']
            fav = serializer.data.get('fav')
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        book = Book()
        book.Author = author
        book.store_name = store_name
        book.description = description
        book.image = image
        book.fav = fav
        book.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        query = Book.objects.filter(store_name__contains=search)
        serializer = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def delete(self, request, pk):
        query = Book.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
