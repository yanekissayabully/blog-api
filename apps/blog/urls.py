from rest_framework.routers import DefaultRouter

from django.urls import include, path

from apps.blog.views import CategoryViewSet, CommentViewSet, PostViewSet, TagViewSet

app_name = 'blog'

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('tags', TagViewSet, basename='tag')
router.register('posts', PostViewSet, basename='post')

comment_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy',
})

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', comment_list, name='post-comments-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', comment_detail, name='post-comments-detail'),
]
