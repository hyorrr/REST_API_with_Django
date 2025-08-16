from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from drf_projects.watchmate.watchlist_app.api.serializers import MovieSerializer
from rest_framework import status

from rest_framework.views import APIView

class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class MovieDetailAV(APIView):
    
    def get(self, request, pk):
        
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        
        movie = Movie.objects.get(pk=pk)
        movie.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     # GET: 유저가 정보 요청하면 보여주기
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         # MovieSerializer()는 기본적으로 "하나의 객체"만 직렬화할 수 있음
#         # many=True => Movie.objects.all(), filter() 등으로 여러 개의 객체(QuerySet) 를 가져올 때 필요      
#         return Response(serializer.data)
    
#     # POST: user가 정보를 보면 데터 저장하기
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
        
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     # put: update every single field in data
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         # serializer = MovieSerializer(data=request.data) # 새로운 인스턴스를 생성하는 방식
#         serializer = MovieSerializer(movie, data=request.data) # 기존 객체를 수정하는 방식, 기존 인스턴스 movie를 넘겨줌
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) # 200 code
#         else:
#             # return Response(serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete() # HTTP_204_NO_CONTENT
#         return Response(status=status.HTTP_204_NO_CONTENT)