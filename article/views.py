from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Article
from .models import Author
from .serializers import AuthorSerializer
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets



#region CRUD with function base view
@api_view(['GET','POST'])
def all_articles(request:Request):
    if request.method=='GET':
        articles=Article.objects.order_by('rank').all()
        article_serializer=ArticleSerializer(articles,many=True)
        return Response(article_serializer.data,status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data,status.HTTP_201_CREATED)

    return Response(None, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_crud_view(request:Request,article_id:int):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=ArticleSerializer(article)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_202_ACCEPTED)
        return Response(None,status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        article.delete()
        return Response(None,status.HTTP_204_NO_CONTENT)
#endregion


#region CRUD with Class base view
class ArticleCreateListApiview(APIView):
    def get (self,request:Request):
        articles = Article.objects.order_by('rank').all()
        article_serializer = ArticleSerializer(articles, many=True)
        return Response(article_serializer.data, status.HTTP_200_OK)
    def post (self,request:Request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)

class ArticleRetriveUpdateDeleteApiview(APIView):
    def get_object (self, article_id: int):
        try:
            article = Article.objects.get(pk=article_id)
            return article
        except Article.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)
    def get(self,request:Request, article_id: int):
        article=self.get_object(article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status.HTTP_200_OK)
    def put(self,request:Request, article_id: int):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status.HTTP_202_ACCEPTED)
        return Response(None,status.HTTP_400_BAD_REQUEST)
    def delete(self,request:Request, article_id: int):
        article = self.get_object(article_id)
        article.delete()
        return Response(None,status.HTTP_204_NO_CONTENT)
#endregion

#region CRUD with mixins

class ArticleCreateListMixinApiview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class ArticleRetrievUpdateDeleteMixinApiview(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

#endregion

#region CRUD with generics
class ArticleCreateListGenericApiview(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrievUpdateDeleteGenericApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


#endregion

#region CRUD with viewset
class ArticleCrudViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
#endregion

#region author
class AuthorCreateListGenericApiview(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrievUpdateDeleteGenericApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#endregion

    


