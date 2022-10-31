from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import BatchSerializer
from . models import Batch

# Create your views here.
class BatchApiView(APIView):
    def get(self, request):
        # obj = Batch.objects.select_related()
        batch = Batch.objects.prefetch_related('trainee','trainer').select_related()
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   





































































































# class ArticleApiView(APIView):
    
    
#     def post(self, request):        
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    
    
# class ArticleApiDetails(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, id):
#         try:
#             article = Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(f'Article no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, id):
#         try:
#             article = Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(f'Article no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         try:
#             article = Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(f'Article no {id} is not found'.format(id), status=status.HTTP_404_NOT_FOUND)        
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    