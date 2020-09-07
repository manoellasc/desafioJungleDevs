from django.urls import include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views
import posts.views
import comments.views


router = DefaultRouter()
router.register(r'topics', views.TopicViewSet, basename='topics')

topic_router = routers.NestedSimpleRouter(router, r'topics', lookup='topics')
topic_router.register(r'posts', posts.views.PostViewSet, basename='posts')

posts_router = routers.NestedSimpleRouter(topic_router, r'posts', lookup='posts')
posts_router.register(r'comments', comments.views.CommentViewSet, basename='comments')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(posts_router.urls)),
]