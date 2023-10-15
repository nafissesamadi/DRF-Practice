from rest_framework import serializers
from .models import Article
from .models import Author

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model=Author
        fields='__all__'