from django.shortcuts import render
from article.models import Article
from django.http import  JsonResponse, HttpResponse, HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return HttpResponse('Hello every body. I am trying to learn Django')

@api_view(['GET'])
def ArticlesJson(request: Request):
    articles = list(Article.objects.order_by('rank').all())
    return Response({'articles': articles}, status.HTTP_200_OK)

