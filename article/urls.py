from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ArticleCrudViewset)

urlpatterns = [
    path('',views.all_articles),
    path('<int:article_id>', views.article_crud_view),
    path('cbv/',views.ArticleCreateListApiview.as_view()),
    path('cbv/<int:article_id>', views.ArticleRetriveUpdateDeleteApiview.as_view()),
    path('mixins/',views.ArticleCreateListMixinApiview.as_view()),
    path('mixins/<pk>', views.ArticleRetrievUpdateDeleteMixinApiview.as_view()),
    path('generics/',views.ArticleCreateListGenericApiview.as_view()),
    path('generics/<pk>', views.ArticleRetrievUpdateDeleteGenericApiview.as_view()),
    path('viewsets/', include(router.urls)),
    path('authors/',views.AuthorCreateListGenericApiview.as_view()),
    path('authors/<pk>', views.AuthorRetrievUpdateDeleteGenericApiview.as_view()),

]