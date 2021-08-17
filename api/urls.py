from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename="posts")
router.register(r'groups', views.GroupViewSet, basename="groups")
router.register(r'follow', views.FollowViewSet, basename="follow")
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, basename="comments"
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
