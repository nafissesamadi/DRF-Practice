from django.contrib import admin
from . import models



# Register your models here.
@admin.register((models.Article))
class ArticleAdmin (admin.ModelAdmin):
    pass

@admin.register((models.Author))
class AuthorAdmin (admin.ModelAdmin):
    pass